import numpy as np
import cv2

class ImageEffects:
    def __init__(self):
        pass
    
    def crop(self, img, x, y, w, h):
        return img[y:y+h, x:x+w]
        
    def work(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        ret,thresh = cv2.threshold(blur,120,255,cv2.THRESH_BINARY_INV)
        return thresh
        
