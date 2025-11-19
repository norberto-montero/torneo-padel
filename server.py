#!/usr/bin/env python3
"""
Servidor simple para servir la página web del torneo de pádel
Ejecutar: python server.py
"""

import http.server
import socketserver
import os
import webbrowser
import socket
from pathlib import Path

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/torneo_padel.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def get_local_ip():
    """Obtiene la IP local de la máquina"""
    try:
        # Conecta a un servidor remoto para obtener la IP local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def main():
    # Cambiar al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = MyHTTPRequestHandler
    local_ip = get_local_ip()
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 60)
        print(f"🎾 KE BOLAAAAASO - Servidor iniciado")
        print("=" * 60)
        print(f"\n💻 Para acceder desde esta computadora:")
        print(f"   http://localhost:{PORT}")
        print(f"\n📱 Para acceder desde tu iPhone:")
        print(f"   1. Asegúrate de que tu iPhone esté en la misma red Wi-Fi")
        print(f"   2. Abre Safari en tu iPhone")
        print(f"   3. Ingresa esta URL: http://{local_ip}:{PORT}")
        print("=" * 60)
        print(f"\n⏹️  Presiona Ctrl+C para detener el servidor\n")
        
        # Abrir navegador automáticamente
        webbrowser.open(f'http://localhost:{PORT}/torneo_padel.html')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Servidor detenido. ¡Hasta luego!")

if __name__ == "__main__":
    main()
