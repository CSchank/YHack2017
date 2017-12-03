import socketserver

from http.server import BaseHTTPRequestHandler

def some_function():
    print ("some_function got called")

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            some_function()
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.send_response(200)
        self.wfile.write(bytes("Hello!",'utf-8'))
        return

httpd = socketserver.TCPServer(("", 8080), MyHandler)
httpd.serve_forever()