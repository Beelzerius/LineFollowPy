import numpy as np
import cv2

class Camera:
    
    def __init__(self,cam,w,h):
        self.video_capture = cv2.VideoCapture(cam)
        self.video_capture.set(3, w)
        self.video_capture.set(4, h)
    
    def captureFrame(self):
        ret, frame = self.video_capture.read()
        return frame
        

