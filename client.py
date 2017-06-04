#!/usr/bin/python

import socket
import sys
import random

UDP_IP = "127.0.0.1"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 0))

#SERVER_HOST = raw_input('Inserire IP server: ')

# send xid and hello message
xid = random.randint(1, 65535)
xid_s = str(xid)
print('xid: ' + xid_s)
hello = xid_s + '\n' + 'Hello'
# C1 ---------------------------------------------------------------------------
sock.sendto(hello, (UDP_IP, SERVER_PORT))

# receive ack from server
data, addr = sock.recvfrom(1024)
try:
    xid_s, ack = data.split('\n')
except ValueError:
    print(data)
    sys.exit(1)

# receive 'Registered' from server and send request
if ack == 'Registered':
    print(data)
    a = raw_input('Inserire primo numero: ')
    b = raw_input('Inserire secondo numero: ')
    c = raw_input('Inserire numero: ')

	# send op
    m = xid_s + '\n' + a + '\n' + b + '\n' + c
    # C2 -----------------------------------------------------------------------
    sock.sendto(m, (UDP_IP, SERVER_PORT))

    # receive and print result
    data, addr = sock.recvfrom(1024)
    print(data)

