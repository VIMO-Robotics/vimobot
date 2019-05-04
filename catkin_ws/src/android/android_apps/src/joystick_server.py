#!/usr/bin/env python

# UTP

import socket,traceback
import time

host=""
port=5001
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))

while 1:
    data=s.recvfrom(1024)
    print str(data)   