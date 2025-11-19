# 🚀 Guía: Publicar en GitHub Pages

## 📋 Pasos para publicar tu proyecto

### 1. Crear un repositorio en GitHub

1. Ve a https://github.com y crea una cuenta (si no tienes una)
2. Haz clic en el botón **"New"** o **"+"** → **"New repository"**
3. Nombre del repositorio: `torneo-padel` (o el nombre que prefieras)
4. Marca como **Público** (necesario para GitHub Pages gratuito)
5. **NO** marques "Initialize with README" (ya tienes archivos)
6. Haz clic en **"Create repository"**

### 2. Subir los archivos a GitHub

Tienes dos opciones:

#### Opción A: Usando GitHub Desktop (Más fácil) 🖥️

1. Descarga GitHub Desktop: https://desktop.github.com
2. Instálalo y conéctalo con tu cuenta
3. Ve a **File** → **Add Local Repository**
4. Selecciona la carpeta `torneo-padel`
5. Haz clic en **"Publish repository"**
6. Selecciona el repositorio que creaste
7. Haz clic en **"Publish"**

#### Opción B: Usando Git desde la terminal 💻

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
# Inicializar Git (si no está inicializado)
git init

# Agregar todos los archivos
git add .

# Hacer el primer commit
git commit -m "Initial commit: Torneo de Pádel"

# Conectar con tu repositorio de GitHub
# (Reemplaza TU_USUARIO con tu nombre de usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/torneo-padel.git

# Subir los archivos
git branch -M main
git push -u origin main
```

### 3. Activar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Haz clic en **"Settings"** (Configuración)
3. En el menú lateral izquierdo, busca **"Pages"**
4. En **"Source"**, selecciona:
   - Branch: `main` (o `master`)
   - Folder: `/ (root)`
5. Haz clic en **"Save"**

### 4. ¡Listo! 🎉

GitHub Pages procesará tu sitio (puede tardar 1-2 minutos).

Tu sitio estará disponible en:
```
https://TU_USUARIO.github.io/torneo-padel/
```

**Ejemplo:** Si tu usuario es `juanperez`, tu URL será:
```
https://juanperez.github.io/torneo-padel/
```

### 5. Acceder desde tu iPhone 📱

1. Abre Safari en tu iPhone
2. Ingresa la URL de tu GitHub Pages
3. ¡Funciona perfectamente!

---

## 📁 Archivos necesarios

Asegúrate de tener estos archivos en tu repositorio:

- ✅ `index.html` - Página principal (ya creado)
- ✅ `torneo_padel.html` - También disponible
- ✅ `logo.jpeg` - Logo del torneo
- ✅ `README.md` - Documentación
- ✅ `.nojekyll` - Archivo de configuración (ya creado)

---

## 🔄 Actualizar el sitio

Cada vez que hagas cambios:

### Con GitHub Desktop:
1. Abre GitHub Desktop
2. Verás los cambios en la pestaña "Changes"
3. Escribe un mensaje de commit (ej: "Agregar nueva funcionalidad")
4. Haz clic en **"Commit to main"**
5. Haz clic en **"Push origin"**

### Con Git desde terminal:
```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

Los cambios se reflejarán en GitHub Pages en 1-2 minutos.

---

## ⚠️ Notas importantes

1. **HTTPS automático**: GitHub Pages usa HTTPS automáticamente
2. **URL personalizada**: Puedes usar un dominio personalizado si lo deseas
3. **Límites**: GitHub Pages es gratuito para repositorios públicos
4. **Datos**: Los datos se guardan en localStorage del navegador de cada usuario
5. **Actualizaciones**: Los cambios pueden tardar 1-2 minutos en aparecer

---

## 🐛 Solución de problemas

### El sitio no carga
- Espera 1-2 minutos después de activar Pages
- Verifica que el repositorio sea público
- Verifica que hayas seleccionado la rama correcta (main/master)

### El logo no aparece
- Verifica que `logo.jpeg` esté en la raíz del repositorio
- Verifica que el nombre del archivo sea exactamente `logo.jpeg` (mayúsculas/minúsculas importan)

### Los cambios no se reflejan
- Espera 1-2 minutos
- Limpia la caché del navegador (Ctrl+Shift+R o Cmd+Shift+R)
- Verifica que hayas hecho push de los cambios

---

## ✅ Checklist final

Antes de publicar, verifica:

- [ ] Tienes una cuenta de GitHub
- [ ] Has creado el repositorio
- [ ] Has subido todos los archivos
- [ ] Has activado GitHub Pages en Settings
- [ ] El repositorio es público
- [ ] Tienes `index.html` en la raíz
- [ ] Tienes `logo.jpeg` en la raíz
- [ ] Has esperado 1-2 minutos después de activar Pages

¡Listo para disfrutar tu torneo en la nube! 🎾

