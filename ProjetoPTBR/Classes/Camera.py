import numpy as np
import cv2

class Camera:
    """ Classe reponsavel por capturar imagens """
    
    def __init__(self,cam,w,h):
        """Inicializa a classe criando seus atributos com configurações"""
        
        self.video_capture = cv2.VideoCapture(cam)
        self.video_capture.set(3, w)
        self.video_capture.set(4, h)
    
    def capturarImagem(self):
        """ Captura imagem da camera e retorna """
        
        ret, img = self.video_capture.read()
        return img
        

    #Foram testadas os modelos das seguintes cameras:
    #   NOIR
    #   Powepack VX-17
