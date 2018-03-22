class Program:
    def __init__(self):
        from Config.Config import Config
        self.conf = Config()
        pass
        
    def Execute(self):
        #Initial configs
        conf = self.conf
        
        from Classes.Camera import Camera
        camera = Camera(conf.getConfig("cam"),conf.getConfig("camW"),conf.getConfig("camH"))
        
        from Classes.ImageEfects import ImageEfects
        ImEfc = ImageEfects()
        
        from Classes.LineDetect import LineDetect
        lineD = LineDetect()



        frame = camera.captureFrame()
        
        crop_img = ImEfc.crop(frame,conf.getConfig("imgX"),conf.getConfig("imgY"),conf.getConfig("imgW"),conf.getConfig("imgH"))
        thresh = ImEfc.work(crop_img)
        
        contours = lineD.findContour(thresh)
        answer,cx,cy = lineD.getMov(contours)
        
        cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)

        cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)
        
        cv2.imshow('frame',crop_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            quit()
        
        
        
        
