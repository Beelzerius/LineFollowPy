import numpy as np
import cv2

class ImageEffects:
    
    def crop(self, img, x, y, w, h):
        """ Corta a imagem e retorna """
        
        return img[y:y+h, x:x+w]
        
    def work(self,img):
        """ Transforma a imagem em binaria e retorna """
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        ret,thresh = cv2.threshold(blur,0,255,\
            cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        ret,thresh = cv2.threshold(thresh,0,255,cv2.THRESH_BINARY_INV)
        return thresh, blur
        
    def addLinesContours(self, image, cx, cy, contours, w, h):
        """ Adciona linhas que se cruzam no meio da trilha """
        
        cv2.line(image,(cx,0),(cx,h),(255,0,0),1)
        cv2.line(image,(0,cy),(w,cy),(255,0,0),1)
        cv2.drawContours(image, contours, -1, (0,255,0), 1)
        return image
        
    def resize(self, image, f):
        cv2.resize(image,None,fx=f, fy=f,\
            interpolation = cv2.INTER_CUBIC)
        return image
