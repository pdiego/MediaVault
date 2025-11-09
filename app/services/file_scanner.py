"""
MediaVault - File Scanner Service
Scans directories and detects media files (Single Responsibility)
"""
from pathlib import Path
from typing import List, Optional
from datetime import datetime
import os

from app.models.media import MediaItem, MediaType, Category
from app.config import settings


class FileScanner:
    """Responsible for scanning directories and finding media files"""
    
    def __init__(self):
        self.root_path = settings.root_media_path
        self.media_folders = settings.media_folders
        self.video_extensions = settings.video_extensions
        self.audio_extensions = settings.audio_extensions
        self.document_extensions = settings.document_extensions
    
    def get_categories(self) -> List[Category]:
        """
        Get all available media categories
        Returns list of Category objects
        """
        categories = []
        
        for key, folder_name in self.media_folders.items():
            folder_path = self.root_path / folder_name
            
            # Check if folder exists
            if not folder_path.exists():
                continue
            
            # Count items in folder
            item_count = len(self.scan_folder(folder_path))
            
            category = Category(
                name=key,
                display_name=folder_name,
                path=folder_path,
                item_count=item_count
            )
            categories.append(category)
        
        return categories
    
    def scan_folder(self, folder_path: Path) -> List[Path]:
        """
        Scan a folder and return list of media files
        
        Args:
            folder_path: Path to the folder to scan
            
        Returns:
            List of Path objects for each media file found
        """
        media_files = []
        
        if not folder_path.exists() or not folder_path.is_dir():
            return media_files
        
        # Get all files in folder (not recursive for now)
        try:
            for item in folder_path.iterdir():
                if item.is_file() and self._is_media_file(item):
                    media_files.append(item)
        except PermissionError:
            # Handle permission errors gracefully
            pass
        
        return sorted(media_files, key=lambda x: x.name.lower())
    
    def get_media_items(self, category: str) -> List[MediaItem]:
        """
        Get all media items for a specific category
        
        Args:
            category: Category key (e.g., 'peliculas', 'series')
            
        Returns:
            List of MediaItem objects
        """
        if category not in self.media_folders:
            return []
        
        folder_path = self.root_path / self.media_folders[category]
        file_paths = self.scan_folder(folder_path)
        
        media_items = []
        for file_path in file_paths:
            media_item = self._create_media_item(file_path)
            if media_item:
                media_items.append(media_item)
        
        return media_items
    
    def get_media_item_by_name(self, category: str, filename: str) -> Optional[MediaItem]:
        """
        Get a specific media item by filename
        
        Args:
            category: Category key
            filename: Name of the file
            
        Returns:
            MediaItem object or None if not found
        """
        if category not in self.media_folders:
            return None
        
        folder_path = self.root_path / self.media_folders[category]
        file_path = folder_path / filename
        
        if not file_path.exists() or not file_path.is_file():
            return None
        
        return self._create_media_item(file_path)
    
    def _is_media_file(self, file_path: Path) -> bool:
        """Check if file is a supported media file"""
        extension = file_path.suffix.lower()
        all_extensions = (
            self.video_extensions + 
            self.audio_extensions + 
            self.document_extensions
        )
        return extension in all_extensions
    
    def _get_media_type(self, file_path: Path) -> MediaType:
        """Determine media type based on file extension"""
        extension = file_path.suffix.lower()
        
        if extension in self.video_extensions:
            return MediaType.VIDEO
        elif extension in self.audio_extensions:
            return MediaType.AUDIO
        elif extension in self.document_extensions:
            return MediaType.DOCUMENT
        else:
            return MediaType.UNKNOWN
    
    def _create_media_item(self, file_path: Path) -> Optional[MediaItem]:
        """
        Create a MediaItem from a file path
        
        Args:
            file_path: Path to the media file
            
        Returns:
            MediaItem object or None if error
        """
        try:
            stat = file_path.stat()
            
            media_item = MediaItem(
                name=file_path.stem,  # Filename without extension
                file_path=file_path,
                file_size=stat.st_size,
                created_date=datetime.fromtimestamp(stat.st_ctime),
                modified_date=datetime.fromtimestamp(stat.st_mtime),
                media_type=self._get_media_type(file_path),
                extension=file_path.suffix.lower()
            )
            
            return media_item
            
        except (OSError, PermissionError):
            return None


# Singleton instance
file_scanner = FileScanner()
