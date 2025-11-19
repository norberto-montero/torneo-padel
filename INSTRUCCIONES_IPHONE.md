# 📱 Cómo usar KE BOLAAAAASO en iPhone

## ⚠️ Limitación de iOS

iOS (iPhone/iPad) **no permite abrir archivos HTML locales directamente** por razones de seguridad. Safari bloquea el acceso a archivos locales.

## ✅ Soluciones disponibles

### Opción 1: Usar una app de servidor web GRATUITA (Recomendado)

Hay varias apps **GRATUITAS** que permiten servir archivos localmente desde tu iPhone:

#### **Simple Server: HTTP Server** ⭐ (100% Gratuita)
🔗 **App Store**: https://apps.apple.com/app/simple-server-http-server/id6443893597

1. Descarga "Simple Server: HTTP Server" desde el App Store (es gratuita)
2. Abre la app
3. Sube los archivos (torneo_padel.html, logo.jpeg)
   - Puedes usar AirDrop desde tu Mac o iCloud Drive
4. La app te dará una URL local (ej: `http://192.168.X.X:8080`)
5. Abre esa URL en Safari de tu iPhone
6. ✅ **Ventaja**: Completamente gratuita, sin compras in-app

#### **Web Server for PHP** (Gratuita)
🔗 **App Store**: Busca "Web Server for PHP" en el App Store

1. Descarga la app (gratuita)
2. Permite servir archivos HTML estáticos
3. Similar funcionamiento a Simple Server

#### **Smart HTML Editor with AI** (Gratuita con funciones básicas)
🔗 **App Store**: https://apps.apple.com/app/smart-html-editor-with-ai/id1495364571

- Permite editar y ejecutar HTML directamente
- Puedes copiar el contenido de torneo_padel.html y ejecutarlo
- Incluye preview en tiempo real
- ⚠️ Algunas funciones avanzadas requieren compra

#### **TinyServer** (De pago)
🔗 **App Store**: https://apps.apple.com/app/tinyserver/id1517211662

- ⚠️ Esta app es de pago, pero si ya la tienes funciona perfectamente

### Opción 2: Usar iCloud Drive + Shortcuts

1. Extrae el ZIP en tu Mac
2. Sube `torneo_padel.html` y `logo.jpeg` a iCloud Drive
3. En tu iPhone, abre iCloud Drive
4. Abre el archivo HTML (se abrirá en Safari)
5. ⚠️ **Nota**: Funciona pero con limitaciones (localStorage puede tener problemas)

### Opción 3: Subir el proyecto a la nube (GRATIS) 🌐

Esta es la mejor opción si quieres acceder desde cualquier lugar sin depender de tu Mac:

#### **Netlify Drop** ⭐ (Más fácil - Recomendado)
🔗 **URL**: https://app.netlify.com/drop

1. Ve a https://app.netlify.com/drop
2. Arrastra y suelta la carpeta completa del proyecto (o crea un ZIP con torneo_padel.html y logo.jpeg)
3. ¡Listo! Te dará una URL pública (ej: `https://random-name-123.netlify.app`)
4. Accede desde cualquier dispositivo, incluido tu iPhone
5. ✅ **Ventajas**: 
   - Completamente gratuito
   - HTTPS incluido
   - Sin necesidad de cuenta (aunque puedes crear una para más opciones)
   - Funciona desde cualquier lugar

#### **Vercel** (Muy fácil)
🔗 **URL**: https://vercel.com

1. Ve a https://vercel.com
2. Crea una cuenta gratuita (o usa GitHub)
3. Arrastra la carpeta del proyecto
4. ¡Listo! URL pública automática
5. ✅ **Ventajas**: Muy rápido y fácil

#### **GitHub Pages** (Gratis, requiere cuenta GitHub)
🔗 **URL**: https://pages.github.com

1. Crea una cuenta en GitHub (gratis)
2. Crea un nuevo repositorio
3. Sube los archivos (torneo_padel.html, logo.jpeg)
4. Activa GitHub Pages en la configuración del repositorio
5. Tu sitio estará en: `https://tu-usuario.github.io/tu-repo`
6. ✅ **Ventajas**: Control total, gratis para siempre

#### **Surge.sh** (Gratis, requiere terminal)
🔗 **URL**: https://surge.sh

1. Instala surge: `npm install -g surge`
2. En la carpeta del proyecto, ejecuta: `surge`
3. Te pedirá crear una cuenta (gratis)
4. ¡Listo! URL pública automática
5. ✅ **Ventajas**: Muy rápido, ideal para desarrolladores

### Opción 4: Usar la opción de red local (Ya implementada)

Si tu iPhone y Mac están en la misma Wi‑Fi:
1. Ejecuta `python3 server.py` en tu Mac
2. Usa la URL que muestra el servidor en Safari del iPhone

## 📦 Contenido del ZIP

- `torneo_padel.html` - La aplicación principal
- `logo.jpeg` - Logo del torneo
- `server.py` - Servidor Python (para Mac/PC)
- `README.md` - Documentación

## 🎯 Recomendación

Para uso en iPhone, la **Opción 1** (app Web Server) es la más práctica y funciona completamente offline.

