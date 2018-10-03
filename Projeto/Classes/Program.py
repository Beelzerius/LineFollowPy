import sys
sys.path.append('../')
import cv2
import numpy as np
from Classes.Camera import Camera
from Classes.LineDetect import LineDetect
from Classes.ImageEffects import ImageEffects
from Classes.GpioController import GpioController
from Classes.Screen import Screen
from Config.Config import Config

class Program:
    """ Classe principal do programa """
    
    def __init__(self):
        """ Inicializa a classe criando seus atributos com as configurações"""
        
        self.conf = Config()
        pass



    def Execute(self):
        """ Instancia as demais classes e inicia o while principal """
        
        conf = self.conf
        camera = Camera(conf.getConfig("cam"),conf.getConfig("camW"),\
            conf.getConfig("camH"))
        ImEfc = ImageEffects()
        lineD = LineDetect()
        gC = GpioController(conf.getConfig("Esq"),\
            conf.getConfig("Dir"), conf.getConfig("GpioMode"),\
            conf.getConfig("freq"))
        screen = Screen(conf.getConfig("show"))
        x, y, w, h = conf.getConfig("imgX"), conf.getConfig("imgY"),\
            conf.getConfig("imgW"), conf.getConfig("imgH")
        
        while(True):
            """ Loop principal """
            
            frame = camera.captureFrame()
            crop_img = ImEfc.crop(frame, x, y, w, h)
            thresh, _ = ImEfc.work(crop_img)
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
        
