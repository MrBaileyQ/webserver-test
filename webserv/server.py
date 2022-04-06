from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urls import url_paths

def StartServer(server_host='localhost', server_port=8080):
    # Start the server

    from handle import WebServer
    print("Attempting start server on %s:%s" % (server_host, server_port))

    webServer = HTTPServer((server_host, server_port), WebServer)
    print("Server started http://%s:%s" % (server_host, server_port))

    try:
        print("Starting server...")
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("WOW! You just hit ctrl+c. Exiting.")
        quit()
    except Exception as e:
        print("WOW! I trully am shit at what I do. read the stack trace:")
        print(e)
        quit()


class WebRequest():
    cookies = []
    localstorage = []
    sessionstorage = []
    method = ""
    path = ""
    query = ""

    def __init__(self, ck, ls, ss, m, p, q):
        self.cookies = ck
        self.localstorage = ls
        self.sessionstorage = ss
        self.method = m
        self.path = p
        self.query = q

def get_url(urlpath):
    for i in url_paths:
        if i.path == urlpath:
            return i