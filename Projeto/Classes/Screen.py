import numpy as np
import cv2

class Screen:
    """ Classe responsavel por mostrar imagens e textos """
    
    def __init__ (self, show):
        """ Inicializa a classe criando seus atributos com as configurações"""
        
        self.images = []
        self.show = show



    def printString(self, string):
        """ Saida de texto para o terminal """
        
        if self.show :
            print(string)



    def insertImage(self, index, image):
        """ Insere uma imagem na lista de imagens a serem mostradas """
        
        if self.show :
            self.images.append([index, image])



    def draw(self):
        """ Desenha as imagens da lista na tela e limpa a lista """
        
        if self.show :
            a = 0
            while a < len(self.images):
                index = self.images[a][0]
                image = self.images[a][1]
                cv2.imshow(index, image)
                a += 1
            self.images = []
        
