from RPi import GPIO as gpio
gpio.VERBOSE = True
import time
import cv2

gpio.setmode(gpio.BOARD)

gpio.setup(11, gpio.OUT) #Frente
gpio.setup(13, gpio.OUT) #Esquerda
gpio.setup(15, gpio.OUT) #Direita

direita = False
esquerda = False
frente = False
op = ""

while True:
    op = raw_input()
    if op == "w":
        frente = True
    else: 
        frente = False
    
    if frente:
        gpio.output(11,gpio.HIGH)
    else:
        gpio.output(11,gpio.LOW)


    if op == 'a':
        esquerda = True
    else: 
        esquerda = False
    
    if esquerda:
        gpio.output(13,gpio.HIGH)
    else:
        gpio.output(13,gpio.LOW)
        
        
    if op == 'd':
        direita = True
    else: 
        direita = False
    
    if direita:
        gpio.output(15,gpio.HIGH)
    else:
        gpio.output(15,gpio.LOW)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
