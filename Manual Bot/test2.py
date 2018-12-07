from __future__ import division
from evdev import InputDevice, categorize, ecodes, events
import Adafruit_PCA9685
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
gamepad = InputDevice('/dev/input/event17')

pwmLeft = GPIO.PWM(15, 1000)    #physical 10
directionLeft = 17              #physical 11
pwmRight = GPIO.PWM(18, 1000)   #physical 12
directionRight = 27             #physical 13

GPIO.setup(directionLeft,GPIO.OUT)
GPIO.setup(pwmLeft,GPIO.OUT)
 GPIO.setup(directionRight,GPIO.OUT)
GPIO.setup(pwmRight,GPIO.OUT)

for event in gamepad.read_loop():
     if event.code == 17:
         if event.value == -1:
            GPIO.output(directionLeft,GPIO.HIGH)
            pwmLeft.start(50)
            GPIO.output(directionRight,GPIO.HIGH)              #Forward
            pwmRight.start(50)
         elif event.value == 1:
            GPIO.output(directionLeft,GPIO.LOW)
            pwmLeft.start(50)                                   #Backward
            GPIO.output(directionRight,GPIO.LOW)
            pwmRight.start(50)
         elif event.value == 0:
            GPIO.output(directionLeft,GPIO.LOW)
            pwmLeft.stop()                                      #Stop
            GPIO.output(directionRight,GPIO.LOW)
            pwmRight.stop()
     elif event.code == 16:
         if event.value == -1:
            GPIO.output(directionLeft,GPIO.LOW)
            pwmLeft.start(50)
            GPIO.output(directionRight,GPIO.HIGH)              #Left
            pwmRight.start(50)
         elif event.value == 1:
            GPIO.output(directionLeft,GPIO.HIGH)
            pwmLeft.start(50)
            GPIO.output(directionRight,GPIO.LOW)              #Right
            pwmRight.start(50)
         elif event.value == 0:
            GPIO.output(directionLeft,GPIO.LOW)
            pwmLeft.stop()                                     #stop
            GPIO.output(directionRight,GPIO.LOW)
            pwmRight.stop()