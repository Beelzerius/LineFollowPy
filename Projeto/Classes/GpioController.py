from RPi import GPIO as gpio
gpio.VERBOSE = True
import time
import cv2

class GpioController:
    """ Classe responsavel por administrar a Gpio do Raspberry Pi """
    
    def __init__(self,es,di,mode,freq):
        """ Inicializa a classe criando seus atributos com as configurações"""
        
        gpio.setmode(mode)
        
        self.e = es #Esquerda
        self.d = di #Direita
        
        gpio.setup(self.e, gpio.OUT)
        gpio.setup(self.d, gpio.OUT)
        
        self.pwmEsq = gpio.PWM(self.e,freq)
        self.pwmDir = gpio.PWM(self.d,freq)
        
        self.pwmEsq.start(0)
        self.pwmDir.start(0)
        
        self.es = 0
        self.di = 0
        
    def setDir(self,cont):
        """ Troca o DutyCycle dos pinos para que continue na trilha """
        
        if cont > 80 :
            por = 100 - (((cont-80) * 100) / 80)
            por = round(por)
            if(por == 0):
                if(self.di < self.es):
                    self.pwmDir.ChangeDutyCycle(0)
                    self.pwmEsq.ChangeDutyCycle(100)
                    
                    self.di = 0
                    self.es = 100
                else:
                    self.pwmDir.ChangeDutyCycle(100)
                    self.pwmEsq.ChangeDutyCycle(0)
                    
                    self.di = 100
                    self.es = 0
            else:
                self.pwmDir.ChangeDutyCycle(100)
                self.pwmEsq.ChangeDutyCycle(por)
                
                self.di = por
                self.es = 100
        elif cont < 80 :
            por = (cont * 100) / 80
            por = round(por)
            if(por == 0):
                if(self.di < self.es):
                    self.pwmDir.ChangeDutyCycle(0)
                    self.pwmEsq.ChangeDutyCycle(100)
                    
                    self.di = 0
                    self.es = 100
                else:
                    self.pwmDir.ChangeDutyCycle(100)
                    self.pwmEsq.ChangeDutyCycle(0)
                    
                    self.di = 100
                    self.es = 0
            else:
                self.pwmDir.ChangeDutyCycle(por)
                self.pwmEsq.ChangeDutyCycle(100)
            
                self.di = 100
                self.es = por
        else :
            self.pwmDir.ChangeDutyCycle(100)
            self.pwmEsq.ChangeDutyCycle(100)
            
            self.di = 100
            self.es = 100
            
        out = "D: " + str(self.di) + " E: " + str(self.es)
        return out
        
        
