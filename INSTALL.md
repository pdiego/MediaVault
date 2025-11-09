# 📦 Guía de Instalación - MediaVault

## 🎯 Requisitos previos

### Sistema operativo
- Ubuntu Server 20.04+ (o cualquier distribución Linux compatible)
- Python 3.14 o superior

### Verificar Python
```bash
python3 --version
# Debe mostrar: Python 3.14.x o superior
```

## 🚀 Instalación paso a paso

### 1. Clonar el repositorio

```bash
cd /home/usuario/proyectos
git clone https://github.com/tu-usuario/mediavault.git
cd mediavault
```

### 2. Crear entorno virtual

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Verificar que estás en el entorno virtual
which python
# Debe mostrar: /home/usuario/proyectos/mediavault/venv/bin/python
```

### 3. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurar rutas multimedia

#### Opción A: Usar archivo .env (recomendado)

```bash
# Copiar plantilla de configuración
cp .env.example .env

# Editar con tu editor favorito
nano .env
# o
vim .env
```

Edita la ruta `ROOT_MEDIA_PATH` con la ubicación de tus archivos:

```env
ROOT_MEDIA_PATH=/home/pablo/multimedia
```

#### Opción B: Editar config.py directamente

```bash
nano app/config.py
```

Modifica la línea:
```python
root_media_path: Path = Path("/home/tu_usuario/ROOT")
```

### 5. Organizar tus archivos multimedia

Crea la siguiente estructura de carpetas:

```bash
mkdir -p /home/tu_usuario/ROOT/Peliculas
mkdir -p "/home/tu_usuario/ROOT/Series TV"
mkdir -p /home/tu_usuario/ROOT/Libros
mkdir -p /home/tu_usuario/ROOT/Musica
```

Copia tus archivos multimedia a las carpetas correspondientes:

```bash
# Ejemplo: copiar películas
cp /origen/mis_peliculas/* /home/tu_usuario/ROOT/Peliculas/

# Ejemplo: copiar series
cp -r /origen/mis_series/* "/home/tu_usuario/ROOT/Series TV/"
```

### 6. Probar la instalación

```bash
# Asegúrate de estar en el directorio del proyecto
cd /home/usuario/proyectos/mediavault

# Asegúrate de tener el entorno virtual activado
source venv/bin/activate

# Ejecutar el servidor
python main.py
```

Deberías ver:

```
╔═══════════════════════════════════════╗
║                                       ║
║     🔐 MediaVault v0.1.0             ║
║     Tu bóveda multimedia privada      ║
║                                       ║
╚═══════════════════════════════════════╝

Starting server at http://0.0.0.0:8000

Press CTRL+C to stop
```

### 7. Acceder a la aplicación

Abre tu navegador y ve a:

- **Desde el mismo servidor:** `http://localhost:8000`
- **Desde otra máquina en tu red:** `http://IP_DEL_SERVIDOR:8000`

Ejemplo: `http://192.168.1.100:8000`

## 🔧 Configuración avanzada

### Cambiar puerto

Edita `.env`:
```env
PORT=8080
```

O edita `app/config.py`:
```python
port: int = 8080
```

### Ejecutar en producción

Para uso en producción, es recomendable usar un servidor WSGI como Gunicorn:

```bash
# Instalar Gunicorn
pip install gunicorn

# Ejecutar con Gunicorn
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Ejecutar como servicio systemd

Crea el archivo `/etc/systemd/system/mediavault.service`:

```ini
[Unit]
Description=MediaVault - Sistema de catalogación multimedia
After=network.target

[Service]
Type=simple
User=tu_usuario
WorkingDirectory=/home/tu_usuario/proyectos/mediavault
Environment="PATH=/home/tu_usuario/proyectos/mediavault/venv/bin"
ExecStart=/home/tu_usuario/proyectos/mediavault/venv/bin/python main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Activar el servicio:

```bash
sudo systemctl daemon-reload
sudo systemctl enable mediavault
sudo systemctl start mediavault
sudo systemctl status mediavault
```

## 🐛 Solución de problemas

### El servidor no inicia

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solución:** Asegúrate de tener el entorno virtual activado:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### No aparecen las categorías

**Problema:** La página principal está vacía

**Solución:** Verifica que las rutas en `config.py` o `.env` son correctas y que las carpetas existen:

```bash
ls -la /home/tu_usuario/ROOT/
```

### Error de permisos

**Error:** `PermissionError: [Errno 13] Permission denied`

**Solución:** Asegúrate de que el usuario que ejecuta la aplicación tiene permisos de lectura en las carpetas multimedia:

```bash
chmod -R 755 /home/tu_usuario/ROOT/
```

### No puedo acceder desde otra máquina

**Problema:** No puedo acceder desde `http://192.168.x.x:8000`

**Solución:** Verifica que el firewall permite el puerto 8000:

```bash
# Ubuntu/Debian con UFW
sudo ufw allow 8000
sudo ufw status
```

## 📝 Próximos pasos

1. Añade tus archivos multimedia a las carpetas correspondientes
2. Explora la interfaz web
3. Revisa el [README.md](README.md) para conocer el roadmap futuro
4. Reporta bugs o sugiere mejoras en GitHub Issues

## 💡 Consejos

- **Nombres de archivo:** Usa nombres descriptivos sin caracteres especiales
- **Organización:** Puedes crear subcarpetas dentro de cada categoría
- **Actualización:** Los cambios en carpetas se reflejan automáticamente al recargar la página
- **Backups:** Mantén copias de seguridad de tus archivos multimedia

---

¿Problemas con la instalación? Abre un issue en GitHub o contacta al mantenedor del proyecto.
