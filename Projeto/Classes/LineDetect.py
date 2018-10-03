import numpy as np
import cv2

class LineDetect:
    """ Classe responssavel por detectar a trilha """
    
    def findContour(self, thresh):
        """ Procura pela linha e retorna """
        
        _,contours,hierarchy = cv2.findContours(thresh.copy(), 1,\
            cv2.CHAIN_APPROX_NONE)
        return contours



    def getMov (self,contours):
        """ Encontra o meio da trilha e retorna as cordenadas """
        
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            if(M['m00']!=0):
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            else:
                cx = int(M['m10'])
                cy = int(M['m01'])

        else:
            #Nao consigo ver a linha
            cx = 0
            cy = 0
        
        return cx,cy    
