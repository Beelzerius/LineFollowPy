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
        gC = GpioController(conf.getConfig("AtivaMA"),\
            conf.getConfig("IN1"), conf.getConfig("IN2"),\
            conf.getConfig("AtivaMB"), conf.getConfig("IN3"),\
            conf.getConfig("IN4"), conf.getConfig("GpioMode"),\
            conf.getConfig("freq"))
        screen = Screen(conf.getConfig("show"))
        x, y, w, h = conf.getConfig("imgX"), conf.getConfig("imgY"),\
            conf.getConfig("imgW"), conf.getConfig("imgH")
        
        insert = False;
        while(True):
            """ Loop principal """
            
            frame = camera.captureFrame()
            crop_img = ImEfc.crop(frame, x, y, w, h)
            thresh, _ = ImEfc.work(crop_img)
            contours = lineD.findContour(thresh)
            cx,cy = lineD.getMov(contours)
            if(insert):
                string = gC.setDir(cx)
            else:
                string = gC.onlyShow(cx)
            crop_img = ImEfc.addLinesContours(crop_img, cx, cy,contours,\
                w, h)

            if cv2.waitKey(1) & 0xFF == ord('e'):
                """Fim do programa """
                gC.disableAll()
                insert = False

            if cv2.waitKey(1) & 0xFF == ord('s'):
                """Fim do programa """
                insert = True
            
            screen.insertImage("Crop", crop_img)
            screen.insertImage("Thresh", thresh)
            screen.printString(string + " GPIO: " + str(insert))
            screen.draw()
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                """Fim do programa """
                break
            
