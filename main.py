"""
MediaVault - Main Application
FastAPI application entry point
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.routes import catalogo

# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Tu bóveda multimedia privada - Sistema de catalogación automática",
    debug=settings.debug
)

# Mount static files
app.mount("/static", StaticFiles(directory=str(settings.static_dir)), name="static")

# Include routers
app.include_router(catalogo.router, tags=["catalog"])


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.version
    }


if __name__ == "__main__":
    import uvicorn
    
    print(f"""
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║     🔐 MediaVault v{settings.version}          ║
    ║     Tu bóveda multimedia privada      ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    
    Starting server at http://{settings.host}:{settings.port}
    
    Press CTRL+C to stop
    """)
    
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
