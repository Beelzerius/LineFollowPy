from RPi import GPIO as gpio
gpio.VERBOSE = True
import time
import cv2

class GpioController:
    
    def __init__(self,es,di,mode,freq):
        gpio.setmode(mode)
        
        self.e = es #Esquerda
        self.d = di #Direita
        
        gpio.setup(self.e, gpio.OUT)
        gpio.setup(self.d, gpio.OUT)
        
        self.pwmEsq = gpio.PWM(self.e,freq)
        self.pwmDir = gpio.PWM(self.d,freq)
        
        self.pwmEsq.start(0)
        self.pwmDir.start(0)
        
    def setDir(self,cont):
        if cont > 80 :
            por = 100 - (((cont-80) * 100) / 80)
            print("E: " + str(por))
            
            texto = "E: " + str(por)
            
            self.pwmDir.ChangeDutyCycle(100)
            self.pwmEsq.ChangeDutyCycle(por)
        elif cont < 80 :
            por = (cont * 100) / 80
            print("D: " + str(por))
            
            texto = "D: " + str(por)
            
            self.pwmDir.ChangeDutyCycle(por)
            self.pwmEsq.ChangeDutyCycle(100)
        else :
            self.pwmDir.ChangeDutyCycle(100)
            self.pwmEsq.ChangeDutyCycle(100)
            
            texto = "ambos: 100"
            
        return texto
        
        
