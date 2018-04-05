import socket
import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 10000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print 'Para sair use CTRL+X\n'
msg = raw_input()
while msg <> '\x18':
    ret, frame = video_capture.read()
    udp.sendto (frame, dest)
    msg = raw_input()
udp.close()
