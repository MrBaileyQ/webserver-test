import http
import http.server
import socketserver
import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from server import get_url
from utils import Url

from pages import translate_line

from settings import BASE_DIR

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/crash":
            self.send_response(413)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("I'm a teapot", "utf-8"))
            import time
            time.sleep(1)
            quit()


        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        try:
            print("GET: %s" % self.path)
            url:Url = get_url(self.path)
            print(f"Fetching response for {url}")
            response = url.view_function(self)
            
            print(f"File path: {response.file}")

            html = open(BASE_DIR + response.file, "r")

            for line in html.readlines():
                self.wfile.write(bytes(translate_line(f'{line}', response.context), "utf-8"))

            html.close()
            
        except Exception as ex: 
            self.wfile.write(bytes("Error: %s" % ex, "utf-8"))
            print(ex)
        
    def do_POST(self):
        self.send_response(413)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Im a teapot!", "utf-8"))
