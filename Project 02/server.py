import socket
import numpy as np

HOST = ''              # Endereco IP do Servidor
PORT = 10000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    print msg
udp.close()
