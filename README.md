# 🔐 MediaVault

Tu bóveda multimedia privada. Sistema de catalogación automática de contenido multimedia (películas, series, libros, música) con interfaz web dinámica y simple.

## 🎯 Descripción

Aplicación web que escanea automáticamente carpetas en un servidor Ubuntu y genera un catálogo navegable de archivos multimedia. El sistema detecta nuevos archivos sin necesidad de actualización manual.

## ✨ Características

- **Escaneo automático**: Detecta archivos nuevos sin intervención manual
- **Organización por categorías**: Películas, Series TV, Libros, Música
- **Interfaz web responsive**: Acceso desde cualquier navegador
- **Sin base de datos**: Lectura directa del sistema de archivos
- **Metadata básica**: Información extraída de los archivos
- **Arquitectura SOLID**: Código mantenible y escalable

## 🛠️ Tecnologías

- **Python 3.14**: Lenguaje principal
- **FastAPI**: Framework web moderno y rápido
- **Jinja2**: Motor de plantillas HTML
- **Ubuntu Server**: Sistema operativo host

## 📁 Estructura del Proyecto

```
mediavault/
├── main.py                         # Punto de entrada de la aplicación
├── requirements.txt                # Dependencias Python
├── README.md                       # Este archivo
│
├── app/
│   ├── __init__.py
│   ├── config.py                   # Configuración (rutas de carpetas)
│   │
│   ├── models/                     # Modelos de datos
│   │   ├── __init__.py
│   │   └── media.py                # Clases: Video, Audio, Libro
│   │
│   ├── services/                   # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── file_scanner.py         # Escaneo de carpetas
│   │   └── metadata_extractor.py   # Extracción de metadata
│   │
│   ├── routes/                     # Endpoints de la API
│   │   ├── __init__.py
│   │   └── catalogo.py             # Rutas web
│   │
│   └── templates/                  # Plantillas HTML
│       ├── index.html              # Índice general de categorías
│       ├── listado.html            # Listado de archivos por categoría
│       └── detalle.html            # Detalle de un archivo específico
│
└── static/                         # Recursos estáticos
    ├── css/
    │   └── style.css
    ├── js/
    └── images/
```

## 📂 Organización de Archivos Multimedia

```
ROOT/
├── Peliculas/          # ~200 películas máx.
├── Series TV/          # ~100 series máx.
├── Libros/             # PDFs, EPUBs
└── Musica/             # MP3, FLAC, etc.
```

## 🚀 Instalación

### Requisitos

- Python 3.14+
- Ubuntu Server
- Git

### Pasos

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/mediavault.git
cd mediavault

# Crear entorno virtual
python3.14 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar rutas en app/config.py
# Editar las rutas de tus carpetas multimedia

# Ejecutar la aplicación
python main.py
```

## 💻 Uso

1. Acceder a `http://tu-servidor:8000`
2. Seleccionar categoría (Películas, Series, Libros, Música)
3. Navegar por el listado de archivos
4. Ver detalles de cada archivo

## 🗺️ Roadmap

### Fase 1 (Actual)
- ✅ Estructura del proyecto
- ✅ Definición de arquitectura
- ⏳ Implementación básica
- ⏳ Escaneo de carpetas
- ⏳ Extracción de metadata básica

### Fase 2 (Futura)
- 📅 Integración con APIs externas (TMDb, OMDb, OpenLibrary)
- 📅 Enriquecimiento automático de metadata
- 📅 Portadas y thumbnails
- 📅 Búsqueda y filtrado avanzado
- 📅 Sistema de favoritos

## 🏗️ Principios de Desarrollo

Este proyecto sigue los principios **SOLID**:

- **S**ingle Responsibility: Cada clase tiene una única responsabilidad
- **O**pen/Closed: Abierto a extensión, cerrado a modificación
- **L**iskov Substitution: Las subclases pueden sustituir a sus clases base
- **I**nterface Segregation: Interfaces específicas mejor que generales
- **D**ependency Inversion: Depender de abstracciones, no de implementaciones

## 📝 Licencia

[Especifica tu licencia aquí]

## 👤 Autor

Pablo - DevOps Engineer @ Sensia Solutions

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios propuestos.

---

**Versión:** 0.1.0 (En desarrollo)
