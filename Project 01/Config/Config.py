from RPi import GPIO as gpio

class Config:
    def __init__(self):
        #self.conf[''] = 
        self.conf = {}
        self.conf['cam'] = -1               #Default: -1
        self.conf['camW'] = 160             #Default: 160
        self.conf['camH'] = 120             #Default: 120
        self.conf['imgX'] = 0               #Default: 0
        self.conf['imgY'] = 60              #Default: 60
        self.conf['imgW'] = 160             #Default: 160
        self.conf['imgH'] = 60              #Default: 60
        self.conf['Esq'] = 16               #Default: 16
        self.conf['Dir'] = 18               #Default: 18
        self.conf['GpioMode'] = gpio.BOARD  #Default: gpio.BOARD
        self.conf['freq'] = 100             #Default: 100
        
    def getConfig(self,atr):
        return self.conf[atr]
