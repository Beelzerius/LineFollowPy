class Config:
    def __init__(self):
        #self.conf[''] = 
        self.conf = {}
        self.conf['cam'] = -1
        self.conf['camW'] = 160
        self.conf['camH'] = 120
        self.conf['imgX'] = 0 
        self.conf['imgY'] = 60
        self.conf['imgW'] = 160
        self.conf['imgH'] = 60
        self.conf['Esq'] = 13
        self.conf['Dir'] = 15
        
    def getConfig(self,atr):
        return self.conf[atr]
