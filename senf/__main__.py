"""
file: __main__.py

This file starts senf
"""

from http.server import HTTPServer
from .server import SenfServer

WEB_ROOT = "public_html/"
HOSTNAME = "localhost"
PORT = 8080


def start(hostname, port):
    """Start SenfServer with given hostname and port
    """
    # Initialize and start server
    main_server = HTTPServer((HOSTNAME, PORT), SenfServer)
    main_server.serve_forever()


if __name__ == "__main__":
    start(HOSTNAME, PORT)
