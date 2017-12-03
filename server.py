#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
import simplejson
import numpy as np
from processData import genCatStr
from fitData import fitData
#

PORT_NUMBER = 80


# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        # Send the html message
        if self.path == "/" or self.path == "index.html":
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            f = open("index.html","r")
            fstr = bytes(f.read(),"utf-8")
            self.wfile.write(fstr)
        elif self.path[0:3] == "/js":
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            f = open("js"+self.path[3:],"r")
            fstr = f.read()
            self.wfile.write(fstr)
        else:
            self.wfile.write(b"Goodbye world!")
        return

    def do_POST(self):
        if self.path == "/quote":
            print(self.headers)
            length = int(self.headers["Content-Length"])
            request = str(self.rfile.read(length), "utf-8")
            print("Request: %s" % request)
            reqdict = simplejson.loads(request)
            print(reqdict)
            age = reqdict["age"]
            sex = reqdict["sex"]
            height = reqdict["height"]
            weight = reqdict["weight"]
            state = reqdict["state"]
            long = reqdict["longitude"]
            lat = reqdict["latitude"]
            marst = reqdict["maritalstatus"]
            tobac = reqdict["tobacco"]
            peepcv = reqdict["dependents"]
            optins = reqdict["total"]
            anninc = reqdict["annualincome"]
            preconds = genCatStr(reqdict["medical"])

            linestr = "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d," % (0, age, sex, height, weight, state, long, lat, marst, tobac, optins, anninc, peepcv)
            linestr += genCatStr(preconds)
            print(len(linestr))

            bronze, silver, gold, platinum, purch = fitData(linestr)

            returndict={"bronze": 0
                       ,"silver": 0
                       ,"gold": 0
                       ,"platinum": 0
                       ,"purchase": 0}
            returndict["bronze"] = bronze
            returndict["silver"] = silver
            returndict["gold"]   = gold
            returndict["platinum"] = platinum
            returndict["purchase"] = round(purch)

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

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
        self.send_header("Access-Control-Max-Age", "36000")
        self.end_headers()
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
