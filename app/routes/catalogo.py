"""
MediaVault - Catalog Routes
Web routes for browsing media catalog
"""
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import settings
from app.services.file_scanner import file_scanner
from app.services.metadata_extractor import metadata_extractor

router = APIRouter()
templates = Jinja2Templates(directory=str(settings.templates_dir))


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Home page - Shows all available categories
    """
    categories = file_scanner.get_categories()
    
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "app_name": settings.app_name,
            "categories": categories
        }
    )


@router.get("/categoria/{category_name}", response_class=HTMLResponse)
async def list_media(request: Request, category_name: str):
    """
    List all media items in a category
    
    Args:
        category_name: Category key (peliculas, series, libros, musica)
    """
    # Validate category exists
    if category_name not in settings.media_folders:
        raise HTTPException(status_code=404, detail="Category not found")
    
    # Get all media items in category
    media_items = file_scanner.get_media_items(category_name)
    
    # Get category info
    categories = file_scanner.get_categories()
    current_category = next(
        (cat for cat in categories if cat.name == category_name),
        None
    )
    
    return templates.TemplateResponse(
        "listado.html",
        {
            "request": request,
            "app_name": settings.app_name,
            "category": current_category,
            "media_items": media_items
        }
    )


@router.get("/detalle/{category_name}/{filename:path}", response_class=HTMLResponse)
async def media_detail(request: Request, category_name: str, filename: str):
    """
    Show details of a specific media item
    
    Args:
        category_name: Category key
        filename: Name of the media file
    """
    # Validate category exists
    if category_name not in settings.media_folders:
        raise HTTPException(status_code=404, detail="Category not found")
    
    # Get media item
    media_item = file_scanner.get_media_item_by_name(category_name, filename)
    
    if not media_item:
        raise HTTPException(status_code=404, detail="Media file not found")
    
    # Get metadata
    metadata = metadata_extractor.extract_metadata(media_item)
    
    return templates.TemplateResponse(
        "detalle.html",
        {
            "request": request,
            "app_name": settings.app_name,
            "category_name": category_name,
            "media_item": media_item,
            "metadata": metadata
        }
    )


@router.get("/api/categories")
async def api_categories():
    """
    API endpoint: Get all categories as JSON
    """
    categories = file_scanner.get_categories()
    return [cat.to_dict() for cat in categories]


@router.get("/api/media/{category_name}")
async def api_media_list(category_name: str):
    """
    API endpoint: Get all media items in a category as JSON
    """
    if category_name not in settings.media_folders:
        raise HTTPException(status_code=404, detail="Category not found")
    
    media_items = file_scanner.get_media_items(category_name)
    return [item.to_dict() for item in media_items]
