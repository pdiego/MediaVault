# 🚀 MediaVault - Inicio Rápido

## ✅ Archivos creados

El proyecto **MediaVault** está completo y listo para usar. Incluye:

### 📄 Documentación
- `README.md` - Descripción completa del proyecto
- `INSTALL.md` - Guía detallada de instalación paso a paso
- Este archivo - Inicio rápido

### ⚙️ Configuración
- `.gitignore` - Archivos excluidos de Git
- `.env.example` - Plantilla de configuración
- `requirements.txt` - Dependencias Python
- `app/config.py` - Configuración de la aplicación

### 🔧 Código fuente
- `main.py` - Punto de entrada de la aplicación FastAPI

#### Modelos (`app/models/`)
- `media.py` - Clases de datos: MediaItem, VideoItem, AudioItem, DocumentItem, Category

#### Servicios (`app/services/`)
- `file_scanner.py` - Escaneo de carpetas y archivos
- `metadata_extractor.py` - Extracción de metadata (Fase 2)

#### Rutas (`app/routes/`)
- `catalogo.py` - Endpoints web y API REST

#### Templates (`app/templates/`)
- `index.html` - Página principal con categorías
- `listado.html` - Listado de archivos por categoría
- `detalle.html` - Detalle de cada archivo

#### Estilos (`static/`)
- `static/css/style.css` - Estilos CSS modernos y responsive

---

## 🏃 Inicio rápido (5 minutos)

### 1️⃣ Descargar archivos
```bash
# Descarga el archivo mediavault.tar.gz
# Extrae los archivos en tu servidor Ubuntu
tar -xzf mediavault.tar.gz
cd mediavault
```

### 2️⃣ Instalar dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Configurar rutas
```bash
# Copiar y editar configuración
cp .env.example .env
nano .env

# Cambiar esta línea con tu ruta:
# ROOT_MEDIA_PATH=/home/pablo/ROOT
```

### 4️⃣ Crear estructura de carpetas
```bash
mkdir -p ~/ROOT/Peliculas
mkdir -p ~/ROOT/"Series TV"
mkdir -p ~/ROOT/Libros
mkdir -p ~/ROOT/Musica
```

### 5️⃣ Ejecutar
```bash
python main.py
```

Abre tu navegador: **http://localhost:8000**

---

## 📋 Checklist de configuración

- [ ] Python 3.14+ instalado
- [ ] Entorno virtual creado y activado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Archivo `.env` configurado con rutas correctas
- [ ] Carpetas multimedia creadas
- [ ] Archivos multimedia copiados a las carpetas
- [ ] Servidor ejecutándose (`python main.py`)
- [ ] Navegador abierto en http://localhost:8000

---

## 🎯 Próximos pasos

### Para desarrollo
1. Lee `README.md` para entender la arquitectura
2. Revisa `INSTALL.md` para configuración avanzada
3. Explora el código en `app/` para personalizaciones

### Para producción
1. Cambia `DEBUG=false` en `.env`
2. Configura systemd service (ver INSTALL.md)
3. Configura firewall para el puerto 8000
4. Considera usar Nginx como reverse proxy

### Funcionalidades futuras (Fase 2)
- Integración con TMDb/OMDb para películas
- OpenLibrary para libros
- Tags ID3 para música
- Portadas y thumbnails
- Sistema de búsqueda
- Favoritos

---

## 📞 Soporte

¿Problemas? Revisa:
1. `INSTALL.md` - Sección "Solución de problemas"
2. GitHub Issues
3. Logs del servidor

---

## 🎉 ¡Listo!

Tu **MediaVault** está configurado siguiendo las mejores prácticas:
- ✅ Arquitectura SOLID
- ✅ Python 3.14
- ✅ FastAPI + Jinja2
- ✅ Código limpio y documentado
- ✅ Responsive design
- ✅ Sin base de datos (lectura directa)

**¡Disfruta de tu catálogo multimedia privado!** 🔐
