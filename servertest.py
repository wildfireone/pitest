import socket
import os
import socket
from urlparse import urlparse

HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
listen_socket.bind((HOST,PORT))
listen_socket.listen(1)
print 'serving'
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
    value = 800

    if "Brian" in request:
        http_response = """\
HTTP/1.1 200 OK

Brian wants """ + str(value) +""" margaritas"""
    else:
        http_response = """\
HTTP/1.1 200 OK

<p>giggidy</p> """
    client_connection.sendall(http_response)
    client_connection.close()
            
