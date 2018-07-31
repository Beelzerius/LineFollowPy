import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')
import numpy as np
import cv2
from Classes.Camera import Camera
from Classes.LineDetect import LineDetect
from Classes.ImageEffects import ImageEffects
from Classes.GpioController import GpioController
from Config.Config import Config

class Program:
    def __init__(self):
        self.conf = Config()
        pass
        
    def Execute(self):
        #Initial configs
        conf = self.conf
        
        camera = Camera(conf.getConfig("cam"),conf.getConfig("camW"),conf.getConfig("camH"))
        
        ImEfc = ImageEffects()
        
        lineD = LineDetect()
        
        gC = GpioController(conf.getConfig("Esq"),conf.getConfig("Dir"))
        
        while(True):
            frame = camera.captureFrame()
            crop_img = ImEfc.crop(frame,conf.getConfig("imgX"),conf.getConfig("imgY"),conf.getConfig("imgW"),conf.getConfig("imgH"))
            thresh = ImEfc.work(crop_img)
            
            contours = lineD.findContour(thresh)
            cx,cy = lineD.getMov(contours)
            
            gC.setDir(cx)
            
            cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
            cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)

            cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)
            cv2.imshow('frame',crop_img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("foi 3")
                break
        
        
        
        
        
