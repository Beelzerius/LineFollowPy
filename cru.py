#import RPi.GPIO as GPIO
from RPi import GPIO as GPIO
GPIO.VERBOSE = True  
import time
import cv2
import numpy as np

#set the GPIO pins of raspberry pi.
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)
#enable
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
#setting the GPIO pin as Output
GPIO.setup (24, GPIO.OUT)
GPIO.setup (23, GPIO.OUT)
GPIO.setup (27, GPIO.OUT)
GPIO.setup (22, GPIO.OUT)
#GPIO.PWM( pin, frequency ) it generates software PWM
PWMR = GPIO.PWM (24, 100)
PWMR1 = GPIO.PWM (23, 100)
PWML = GPIO.PWM (27, 100)
PWML1 = GPIO.PWM (22, 100)
#Starts PWM at 0% dutycycle
PWMR.start (0)
PWMR1.start (0)
PWML.start (0)
PWML1.start (0)
#enable pins of the motor
GPIO.output(16, GPIO.HIGH)
GPIO.output(20, GPIO.HIGH)


capture = cv2.VideoCapture(0)  #read the video
capture.set(3,320.0) #set the size
capture.set(4,240.0)  #set the size
capture.set(5,15)  #set the frame rate
for i in range(0,2):
    flag, trash = capture.read() #starting unwanted null value
    

while cv2.waitKey(1) != 27:
    flag, frame = capture.read() #read the video in frames
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#convert each frame to grayscale.
    blur=cv2.GaussianBlur(gray,(9,9),0)#blur the grayscale image
    ret,th1 = cv2.threshold(blur,60,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#using threshold remave noise
    ret1,th2 = cv2.threshold(th1,127,255,cv2.THRESH_BINARY_INV)# invert the pixels of the image frame
    _,contours, hierarchy = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find the contours
    cv2.drawContours(frame,contours,-1,(0,255,0),3)
    cv2.imshow('frame',frame) #show video 
    for cnt in contours:
        if cnt is not None:
            area = cv2.contourArea(cnt)# find the area of contour
            if area>=500 :
                # find moment and centroid
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            
                if cx<=150:
                    l=(cx*100/160)
                    PWMR.start (0)
                    PWML.start (0)
                    PWMR1.ChangeDutyCycle (100)
                    PWML1.ChangeDutyCycle (abs(l-25))
                    time.sleep(.08)
                
                elif cx>=170:
                    r=((320-cx)*100/160)
                    PWMR.start (0)
                    PWML.start (0)
                    PWMR1.ChangeDutyCycle (abs(r-25))
                    PWML1.ChangeDutyCycle (100)
                    time.sleep(.08)
               
                elif cx>151 and cx<169:
                    PWMR.start (0)
                    PWML.start (0)
                    PWMR1.ChangeDutyCycle (96)
                    PWML1.ChangeDutyCycle (100)
                    time.sleep(.3)
                
                else:
                    PWMR1.start (0)
                    PWML1.start (0)
                    PWMR.ChangeDutyCycle (100)
                    PWML.ChangeDutyCycle (100)
                    time.sleep(.08)
            
            else:
                PWMR1.start (0)
                PWML1.start (0)
                PWMR.ChangeDutyCycle (100)
                PWML.ChangeDutyCycle (100)
                time.sleep(.08)
           
        else:
            PWMR1.start (0)
            PWML1.start (0)
            PWMR.ChangeDutyCycle (100)
            PWML.ChangeDutyCycle (100)
            time.sleep(.1)
        
PWMR.start (0)
PWMR1.start (0)                 
PWML.start (0)                 
PWML1.start (0)
        
