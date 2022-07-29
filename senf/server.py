"""
file: server.py

This file contains the senf server
"""

import cgi
from http.server import SimpleHTTPRequestHandler

WEB_ROOT = "public_html/"


class SenfServer(SimpleHTTPRequestHandler):
    """HTTP Server that can accept POST requests"""

    def __init__(self, *args, **kwargs):
        """Initialization of server that changes the web root"""
        super().__init__(*args, **kwargs, directory=WEB_ROOT)

    def do_POST(self):
        """Function to handle POST requests"""

        # Set environ and get form data
        environ = {
            "REQUEST_METHOD": "POST",
            "CONTENT_TYPE": self.headers["Content-Type"],
        }
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ=environ)

        # Save form data
        response = save_form(form)

        # Serve response
        self.send_response(200, "OK")
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(response, "utf-8"))


def save_form(form):
    """Save form data

    This function takes in the form data and handles it accordingly.
    Currently it just prints out two fields and saves the input
    """

    # Get first and last name
    fname = form["firstname"].value
    lname = form["lastname"].value

    # Get file upload
    _file = form["file"].value
    _filename = form["file"].filename

    # Save file
    with open(_filename, "wb") as f:
        f.write(_file)

    return f"Hi {fname} {lname}, I got your data!"
