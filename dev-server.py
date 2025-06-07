import http.server
import socketserver
import webbrowser
import os
from threading import Timer

PORT = 8000
DIRECTORY = "gamezoid"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def open_browser():
    webbrowser.open(f'http://localhost:{PORT}')

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server")
        Timer(1.5, open_browser).start()
        httpd.serve_forever()

if __name__ == "__main__":
    run_server() 