#!/usr/bin/avr python

#Info:
# program: simple port scan and print port
# types IP,  range end way argunment
# mathoian


#use argument ip = sys.argv[1]  port = sys.argv[2]

import sys
import socket


ip = sys.argv[1]
port = int(sys.argv[2])

for port in range(1,port):
    socketCon = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if socketCon.connect_ex((ip,port)) == 0:
        print(f" HOST {ip} PORT OPEN {port}")
        socketCon.close()
