import logging
import http.server
import socketserver

HOST = '0.0.0.0'
PORT = 8000

logger = logging.getLogger(__name__)
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    logger.warning(f'** Serving at: http://{HOST}:{PORT}/ **')
    httpd.serve_forever()