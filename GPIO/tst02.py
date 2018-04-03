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

while True:
    op = raw_input()
    if op == 1:
        frente = True
    else: 
        frente = False
    
    
    if op == 2:
        esquerda = True
    else: 
        esquerda = False
    
    
    if op == 3:
        direita = True
    else: 
        direita = False
    
    print (gpio.input(11))
    if frente:
        gpio.output(11,gpio.HIGH)
    elif gpio.input(11):
        gpio.output(11,gpio.LOW)
        
    if esquerda:
        gpio.output(13,gpio.HIGH)
    elif gpio.input(13):
        gpio.output(13,gpio.LOW)
        
    if direita:
        gpio.output(15,gpio.HIGH)
    elif gpio.input(15):
        gpio.output(15,gpio.LOW)
