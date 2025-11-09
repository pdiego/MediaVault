"""
MediaVault - Metadata Extractor Service
Extracts metadata from media files (Future Phase 2)
"""
from pathlib import Path
from typing import Dict, Optional

from app.models.media import MediaItem, MediaType


class MetadataExtractor:
    """
    Responsible for extracting metadata from media files
    Future implementation will use libraries like:
    - pymediainfo for videos
    - mutagen for audio
    - pypdf for PDFs
    """
    
    def extract_metadata(self, media_item: MediaItem) -> Dict:
        """
        Extract detailed metadata from media file
        
        Args:
            media_item: MediaItem object
            
        Returns:
            Dictionary with extracted metadata
        """
        # TODO: Implement in Phase 2
        # For now, return basic file info
        return {
            "basic_info": media_item.to_dict(),
            "extended_metadata": self._get_placeholder_metadata(media_item)
        }
    
    def _get_placeholder_metadata(self, media_item: MediaItem) -> Dict:
        """
        Placeholder for future metadata extraction
        Returns empty dict for now
        """
        metadata = {}
        
        if media_item.media_type == MediaType.VIDEO:
            metadata = {
                "duration": None,
                "resolution": None,
                "codec": None,
                "fps": None
            }
        elif media_item.media_type == MediaType.AUDIO:
            metadata = {
                "duration": None,
                "bitrate": None,
                "artist": None,
                "album": None,
                "year": None
            }
        elif media_item.media_type == MediaType.DOCUMENT:
            metadata = {
                "page_count": None,
                "author": None,
                "title": None,
                "subject": None
            }
        
        return metadata
    
    def enrich_with_external_api(self, media_item: MediaItem) -> Dict:
        """
        Enrich metadata using external APIs (Phase 2)
        - TMDb for movies/series
        - OMDb as alternative
        - OpenLibrary for books
        
        Args:
            media_item: MediaItem object
            
        Returns:
            Dictionary with enriched metadata
        """
        # TODO: Implement in Phase 2
        return {
            "source": "Not implemented yet",
            "data": {}
        }


# Singleton instance
metadata_extractor = MetadataExtractor()
