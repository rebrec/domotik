#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import serial;
import time;


def allume():
    start=end=time.time()
    while ((ser.readline()  != 'Commande : ON\r\n') and (end-start<3)):
        ser.write("ON\r".encode());
        time.sleep(0.5);
        end=time.time();
    if end-start > 3:
        print "Delais maximum atteint"
    msg='Allumage acquite';
    ser.flushInput()
    return msg;

def eteint():
    start=end=time.time()
    while ((ser.readline()  != 'Commande : OFF\r\n') and (end-start<3)):
        ser.write("OFF\r".encode());
        time.sleep(0.5);
        end=time.time();
    if end-start > 3:
        print "Delais maximum atteint"
    msg='Extinction acquite';
    ser.flushInput()
    return msg;



#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        msg ='';
        if self.path=="/seton":
            msg=allume();
        elif self.path=="/setoff":
            msg=eteint();

        try:
            if msg == '':
                self.send_error(404,'ERREUR');
            else:
                mimetype='text/html'
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write('<html><head></head><body><h1 style="font-size:150px">' + msg + '</h1></body></html>')
            return


        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

try:
    PORT_NUMBER = 8080
    ser = serial.Serial('/dev/ttyUSB0', 9600);
    eteint()
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
    ser.close();
