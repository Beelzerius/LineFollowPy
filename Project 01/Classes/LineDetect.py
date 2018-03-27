import numpy as np
import cv2

class LineDetect:
    
    def __init__(self):
        pass
    
    def findContour(self, thresh):
        _,contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
        return contours
    
    def getMov (self,contours):
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            if(M['m00']!=0):
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            else:
                cx = int(M['m10'])
                cy = int(M['m01'])

            if cx >= 120:
                #Esquerda
                a = 2

            if cx < 120 and cx > 50:
                #No Caminho 
                a = 1

            if cx <= 50:
                #Direita
                a = 3

        else:
            #Nao consigo ver a linha
            a = 0
            cx = 0
            cy = 0
        
        return a,cx,cy    
