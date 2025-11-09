"""
MediaVault - Configuration
Application settings and paths configuration
"""
from pathlib import Path
from pydantic_settings import BaseSettings
from typing import Dict


class Settings(BaseSettings):
    """Application settings using Pydantic"""
    
    # Application info
    app_name: str = "MediaVault"
    version: str = "0.1.0"
    debug: bool = True
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Media folders configuration
    # Modifica estas rutas según tu servidor
    root_media_path: Path = Path("/home/usuario/ROOT")
    
    media_folders: Dict[str, str] = {
        "peliculas": "Peliculas",
        "series": "Series TV",
        "libros": "Libros",
        "musica": "Musica"
    }
    
    # Supported file extensions
    video_extensions: tuple = (".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm")
    audio_extensions: tuple = (".mp3", ".flac", ".wav", ".aac", ".ogg", ".m4a")
    document_extensions: tuple = (".pdf", ".epub", ".mobi", ".azw3")
    
    # Templates
    templates_dir: Path = Path(__file__).parent / "templates"
    static_dir: Path = Path(__file__).parent.parent / "static"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Singleton instance
settings = Settings()
