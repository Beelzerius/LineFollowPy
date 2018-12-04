from RPi import GPIO as gpio

class Config:
    """ Classe responsavel por gerenciar as configuracoes """
    
    def __init__(self):
        """ Inicializa a classe criando seus atributos com as configuracoes"""
        
        #self.conf[''] = 
        self.conf = {}
        self.conf['show']      =  1          #Padrao:  1
        self.conf['cam']       = -1          #Padrao: -1
        self.conf['camW']      =  160        #Padrao:  160
        self.conf['camH']      =  120        #Padrao:  120
        self.conf['imgX']      =  0          #Padrao:  0
        self.conf['imgY']      =  60         #Padrao:  60
        self.conf['imgW']      =  160        #Padrao:  160
        self.conf['imgH']      =  60         #Padrao:  60
        self.conf['AtivaMA']   =  12         #Padrao:  12
        self.conf['IN1']       =  19         #Padrao:  19
        self.conf['IN2']       =  26         #Padrao:  26
        self.conf['AtivaMB']   =  18         #Padrao:  18
        self.conf['IN3']       =  23         #Padrao:  23
        self.conf['IN4']       =  24         #Padrao:  24
        self.conf['threshold'] =  135        #Padrao:  135
        self.conf['GpioMode']  =  gpio.BCM   #Padrao:  gpio.BCM
        self.conf['freq']      =  100        #Padrao:  100
        
    def getConfig(self,atr):
        """ Retorna a configuração """
        
        return self.conf[atr]
