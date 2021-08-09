# TCP protocol is built on top on the IP(Internet Protocol)
# TCP Connection / Sockets

# TCP Port numbers: A port is an application-specific or process-specific software communication endpoint
# It allow multiple networked applications to coexist on the same server.
# There is a list of well-known TCP port numbers.

# There is a list of well-known TCP port numbers:
# Email: 25
# Login: 80

# Sockets in python
# Python has built-in support for TCP Sockets

import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_socket.send(cmd)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
my_socket.close()

# HTTP Protocol: Application layer protocol
# Invented for the Web: To retrieve HTML, Images, Documents, etc.
