#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
import simplejson
import numpy as np
from processData import genCatStr

PORT_NUMBER = 8080


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
        if self.path == "/quote":
            length = int(self.headers["Content-Length"])
            request = str(self.rfile.read(length), "utf-8")
            reqdict = simplejson.loads(request)
            print(reqdict)
            age = reqdict["age"]
            sex = reqdict["sex"]
            height = reqdict["height"]
            weight = reqdict["weight"]
            state = reqdict["state"]
            long = reqdict["longitude"]
            lat = reqdict["latitude"]
            marst = reqdict["marital"]
            tobac = reqdict["tobacco"]
            peepcv = reqdict["dependents"]
            anninc = reqdict["annualincome"]
            medical = genCatStr(simplejson.loads(reqdict["medical"]))

            linestr = "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d," % (0, age, sex, height, weight, state, long, lat, marst, tobac, optins, anninc, peepcv)

            returndict={"bronze": 0
                       ,"silver": 0
                       ,"gold": 0
                       ,"platinum": 0
                       ,"purchase": 0}

            returnjson = simplejson.dumps(returndict)

            response = bytes(returnjson, "utf-8")  # create response

            self.send_response(200)  # create header
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()

            self.wfile.write(response)  # send response
            return
        else:
            self.send_response(404)
            return


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port', PORT_NUMBER)

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()
    print('^C received, shutting down the web server')