import sys
sys.path.append('../')
import cv2
import numpy as np
from Classes.Camera import Camera
from Classes.DetectorDeLinhas import DetectorDeLinhas
from Classes.Efeitos import Efeitos
from Classes.ControladorGpio import ControladorGpio
from Classes.Graficos import Graficos
from Config.Configuracoes import Configuracoes

class Programa:
    """ Classe principal do programa """
    
    def __init__(self):
        """ Inicializa a classe criando seus atributos com as configurações"""
        
        self.conf = Config()
        pass



    def executar(self):
        """ Instancia as demais classes e inicia o while principal """
        
        conf = self.conf
        camera = Camera(conf.getConfig("cam"),conf.getConfig("camW"),\
            conf.getConfig("camH"))
        ImEfc = ImageEffects()
        lineD = LineDetect()
        gC = GpioController(conf.getConfig("AtivaMA"),\
            conf.getConfig("IN1"), conf.getConfig("IN2"),\
            conf.getConfig("AtivaMB"), conf.getConfig("IN3"),\
            conf.getConfig("IN4"), conf.getConfig("GpioMode"),\
            conf.getConfig("freq"))
        screen = Screen(conf.getConfig("show"))
        x, y, w, h = conf.getConfig("imgX"), conf.getConfig("imgY"),\
            conf.getConfig("imgW"), conf.getConfig("imgH")
        
        while(True):
            """ Loop principal """
            
            img = camera.capturarImagem()
            img_cortada = ImEfc.cortar(img, x, y, w, h)
            img_binaria, _ = ImEfc.work(img_cortada)
            contours = lineD.findContour(thresh)
            cx,cy = lineD.getMov(contours)
            string = gC.setDir(cx)
            screen.printString(string)
            crop_img = ImEfc.addLinesContours(crop_img, cx, cy,contours,\
                w, h)
            
            screen.insertImage("Crop", crop_img)
            screen.insertImage("Thresh", thresh)
            screen.draw()
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                """Fim do programa """
                break
        
