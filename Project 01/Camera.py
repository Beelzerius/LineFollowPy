class Camera:
    
    def __init__(self,cam,w,h):
        self.videoCapture = cv2.VideoCapture(cam)
        self.video_capture.set(3, w)
        self.video_capture.set(4, h)
    
    def captureFrame(self):
        ret, frame = video_capture.read()
        return frame
        

