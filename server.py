#!/usr/bin/python

import socket
import math

HOST = 'localhost'
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print('Listening to ' + str(HOST) + ', port: ' + str(PORT))

while True:

    data, addr = sock.recvfrom(1024)
    # check for 302 error
    try:
        xid, hello = data.split('\n')
    except ValueError:
        r = '302 - Wrong values ' + xid
        sock.sendto(r, addr)
        continue
    print('Connection from ' + str(addr) + ', xid: ' + xid)

    if hello == 'Hello':
        response = xid + '\n' + 'Registered'
        # S1 -------------------------------------------------------------------
        sock.sendto(response, addr)

        # receiving operations
        # if gets an hello, returns 301
        data, addr = sock.recvfrom(1024)
        try:
            xid_c, a, b, c = data.split('\n')
        except ValueError:
            r = '302 - Wrong values ' + xid
            sock.sendto(r, addr)
            continue

        # check xids consistency
        # if they're different, discard it and return into loop
        if int(xid) != int(xid_c):
            resp = '301 - Wrong XID ' + xid_c
            sock.sendto(resp, addr)
            continue

        # evaluate operation
        radice = math.sqrt(int(b)**2) - (4 * int(a) * int(c))
        if radice < 0:
            resp = "400 - Errore" + xid
        elif radice == 0:
            resp = "300 - Soluzioni coincidenti " + xid
            coin = (-int(b))/2*int(a)
            resp = "x1 e x2" + str(coin)
        else:
            sol1 = (-int(b) - radice)/2*int(a)
            sol2 = (-int(b) + radice)/2*int(a)
            resp = "x1 = " + str(sol1) + '\n' + "x2 = " + str(sol2)
        # S2 -------------------------------------------------------------------
        sock.sendto(resp, addr)

    # if a hello message doesn't come
    # discard it and return into loop
    else:
        continue
