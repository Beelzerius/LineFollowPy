from RPi import GPIO as gpio
import cv2

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
nn = 12
gpio.setup(nn, gpio.OUT)
pwm = gpio.PWM(nn,100)
gpio.setup(18, gpio.OUT)
pwm2 = gpio.PWM(18,100)
por = 0

pwm.start(0)
pwm2.start(0)

gpio.setup(19, gpio.OUT)
gpio.setup(26, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
while(True):
    print(str(por) + "%")
    por = por + int(input("Soma : "))
    gpio.output(19, True)
    gpio.output(26, False)
    gpio.output(23, True)
    gpio.output(24, False)
    pwm.ChangeDutyCycle(por)
    pwm2.ChangeDutyCycle(0)
