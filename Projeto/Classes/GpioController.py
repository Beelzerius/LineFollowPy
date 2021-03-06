from RPi import GPIO as gpio
gpio.VERBOSE = True
import time
import cv2

class GpioController:
    """ Classe responsavel por administrar a Gpio do Raspberry Pi """
    
    def __init__(self, es, in1, in2, di, in3, in4, mode, freq):
        """ Inicializa a classe criando seus atributos com as configurações"""
        
        gpio.setmode(mode)
        
        self.e = es #Esquerda
        self.in1 = in1
        self.in2 = in2
        
        self.d = di #Direita
        self.in3 = in3
        self.in4 = in4
        
        gpio.setup(self.e, gpio.OUT)
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)
        
        gpio.setup(self.d, gpio.OUT)
        gpio.setup(self.in3, gpio.OUT)
        gpio.setup(self.in4, gpio.OUT)
        
        self.pwmEsq = gpio.PWM(self.e,freq)
        self.pwmDir = gpio.PWM(self.d,freq)
        
        
        self.pwmEsq.start(0)
        self.pwmDir.start(0)
        
        self.es = 0
        self.di = 0
        
    def disableAll(self):
        """Desliga todos os pinos"""
        gpio.output(self.in1, False)
        gpio.output(self.in2, False)
        gpio.output(self.in3, False)
        gpio.output(self.in4, False)
        self.pwmDir.ChangeDutyCycle(0)
        self.pwmEsq.ChangeDutyCycle(0)

    def onlyShow(self, cont):
        """Só retorna o DC mas não manda para os pinos"""
        if cont > 80 :
            por = 100 - (((cont-80) * 100) / 80)
            por = round(por)
            if(por == 0):
                if(self.di < self.es):
                    self.di = 0
                    self.es = 100
                else:
                    self.di = 100
                    self.es = 0
            else:
                self.di = por
                self.es = 100
        elif cont < 80 :
            por = (cont * 100) / 80
            por = round(por)
            if(por == 0):
                if(self.di < self.es):
                    self.di = 0
                    self.es = 100
                else:
                    self.di = 100
                    self.es = 0
            else:
                self.di = 100
                self.es = por
        else :
            self.di = 100
            self.es = 100
            
        out = "D: " + str(self.di) + "% E: " + str(self.es) + "%"
        return out
        
    def setDir(self, cont):
        """ Troca o DutyCycle dos pinos para que continue na trilha """
        
        gpio.output(self.in1, True)
        gpio.output(self.in2, False)
        gpio.output(self.in3, True)
        gpio.output(self.in4, False)
        
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
        
        
