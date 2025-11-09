"""
MediaVault - Media Models
Data classes for different media types following SOLID principles
"""
from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
from typing import Optional
from enum import Enum


class MediaType(str, Enum):
    """Enum for media types"""
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"
    UNKNOWN = "unknown"


@dataclass
class MediaItem:
    """Base class for all media items (Single Responsibility)"""
    
    name: str
    file_path: Path
    file_size: int  # in bytes
    created_date: datetime
    modified_date: datetime
    media_type: MediaType
    extension: str
    
    @property
    def file_size_mb(self) -> float:
        """Return file size in MB"""
        return round(self.file_size / (1024 * 1024), 2)
    
    @property
    def file_size_gb(self) -> float:
        """Return file size in GB"""
        return round(self.file_size / (1024 * 1024 * 1024), 2)
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "file_path": str(self.file_path),
            "file_size": self.file_size,
            "file_size_mb": self.file_size_mb,
            "file_size_gb": self.file_size_gb,
            "created_date": self.created_date.isoformat(),
            "modified_date": self.modified_date.isoformat(),
            "media_type": self.media_type.value,
            "extension": self.extension
        }


@dataclass
class VideoItem(MediaItem):
    """Video-specific media item"""
    
    # Future: Add video-specific metadata
    duration: Optional[int] = None  # in seconds
    resolution: Optional[str] = None  # e.g., "1920x1080"
    codec: Optional[str] = None
    
    def __post_init__(self):
        self.media_type = MediaType.VIDEO


@dataclass
class AudioItem(MediaItem):
    """Audio-specific media item"""
    
    # Future: Add audio-specific metadata
    duration: Optional[int] = None  # in seconds
    bitrate: Optional[int] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    
    def __post_init__(self):
        self.media_type = MediaType.AUDIO


@dataclass
class DocumentItem(MediaItem):
    """Document-specific media item"""
    
    # Future: Add document-specific metadata
    page_count: Optional[int] = None
    author: Optional[str] = None
    title: Optional[str] = None
    
    def __post_init__(self):
        self.media_type = MediaType.DOCUMENT


@dataclass
class Category:
    """Category/Folder representation"""
    
    name: str
    display_name: str
    path: Path
    item_count: int = 0
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "display_name": self.display_name,
            "path": str(self.path),
            "item_count": self.item_count
        }
