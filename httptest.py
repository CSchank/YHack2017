#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 80


# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        if self.path == "/hello":
            self.wfile.write(b"Hello Sophia!")
        else:
            self.wfile.write(b"Goodbye world!")
        return

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        request = str(self.rfile.read(length), "utf-8")
        print("Data: " + request, "utf-8")

        response = bytes("This is the response. \n" + request, "utf-8")  # create response

        self.send_response(200)  # create header
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)  # send response


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print
    'Started httpserver on port ', PORT_NUMBER

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()
    print('^C received, shutting down the web server')