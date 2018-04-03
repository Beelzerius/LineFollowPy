from RPi import GPIO as gpio
gpio.VERBOSE = True
import time
import cv2

class GpioController:
    
    def __init__(self):
        gpio.setmode(gpio.BOARD)
        
        self.f = 11 #Frente
        self.e = 13 #Esquerda
        self.d = 15 #Direita
        
        gpio.setup(self.f, gpio.OUT)
        gpio.setup(self.e, gpio.OUT)
        gpio.setup(self.d, gpio.OUT)
        
        gpio.output(self.f,False)
        gpio.output(self.e,False)
        gpio.output(self.d,False)
        
    def setDir(self,op):
        
        if op == 1:
            gpio.output(self.f,True)
        else:
            gpio.output(self.f,False)
            
        if op == 2:
            gpio.output(self.e,True)
        else:
            gpio.output(self.e,False)
            
        if op == 3:
            gpio.output(self.d,True)
        else:
            gpio.output(self.d,False)
        
