from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import socket

port=5050
s = socket.socket()
#s.bind(('192.168.43.202', port))
s.bind(('127.0.0.1', port))
s.listen(5)                     # Now wait for client connection.
global data
print 'Server listening....'

 
app = Flask(__name__)
 
@app.route("/")
def index():
    #return "\t\tIoT Smart Plug\nVoltage:220V\nCurrent:5A"
    return " Garnet-A 29   Hi , ANAND THE GREAT!!! No worries @@  Your room is locked"
    #return data     

@app.route("/hello/<string:name>/")
def hello(name):


    return render_template(
        'test.html',name=data)

if __name__ == "__main__":
    
    

    #conn, addr = s.accept()     # Establish connection with client.
    app.run()
   # print 'Got connection from', addr
    #data = conn.recv(1024)
    #data=raw_input("Enter:")
    #print('Server received', repr(data))
   # conn.send("Value Sent")
    

    ##    print "\nEnter:"
    ##    for i in range(0,10):
    ##        conn.send(str(i))


       # print('Done sending')
    #conn.send('Thank you for connecting')
       # app.run(host='127.0.0.1', port=5005)
   # conn.close()
