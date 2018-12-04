from RPi import GPIO as gpio
gpio.VERBOSE = True
import time
import cv2

class ControladorGpio:
    """ Classe responsavel por administrar a Gpio do Raspberry Pi """
    
    def __init__(self, ativaMA, in1, in2, ativaMB, in3, in4, modo, freq):
        """ Inicializa a classe criando seus atributos com as configurações"""
        
        gpio.setmode(mode)
        
        self.ativaMA = ativaMA #MotorA - Esquerda
        self.in1 = in1
        self.in2 = in2
        
        self.ativaMB = ativaMB #MotorB - Direita
        self.in3 = in3
        self.in4 = in4
        
        gpio.setup(self.ativaMA, gpio.OUT)
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)
        
        gpio.setup(self.ativaMB, gpio.OUT)
        gpio.setup(self.in3, gpio.OUT)
        gpio.setup(self.in4, gpio.OUT)
        
        self.pwmEsq = gpio.PWM(self.ativaMA,freq)
        self.pwmDir = gpio.PWM(self.ativaMB,freq)
        
        gpio.output(self.in1, True)
        gpio.output(self.in2, False)
        gpio.output(self.in3, True)
        gpio.output(self.in4, False)
        
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
            
        out = "D: " + str(self.di) + "% E: " + str(self.es) + "%"
        return out
        
        
