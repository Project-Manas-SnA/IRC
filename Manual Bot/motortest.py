from __future__ import division
from evdev import InputDevice, categorize, ecodes, events
import Adafruit_PCA9685
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
gamepad = InputDevice('/dev/input/event0')

GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

pwmLeft = GPIO.PWM(15, 1000)    #physical 10
directionLeft = 17              #physical 11
pwmRight = GPIO.PWM(18, 1000)   #physical 12
directionRight = 27             #physical 13

GPIO.setup(directionLeft,GPIO.OUT)

GPIO.setup(directionRight,GPIO.OUT)

for event in gamepad.read_loop():

    if event.code == 17:

        if event.value == -1:
            GPIO.output(directionLeft,GPIO.HIGH)
            pwmLeft.start(speed)
            GPIO.output(directionRight,GPIO.HIGH)              #Forward
            pwmRight.start(speed)
        elif event.value == 1:
            GPIO.output(directionLeft,GPIO.LOW)
            pwmLeft.start(speed)                                   #Backward
            GPIO.output(directionRight,GPIO.LOW)
            pwmRight.start(speed)


        elif event.value == 0:
            GPIO.output(directionLeft,GPIO.LOW)
            pwmLeft.stop()                                      #Stop
            GPIO.output(directionRight,GPIO.LOW)
            pwmRight.stop()

    elif event.code == 16:

        if event.value == -1:
            GPIO.output(directionLeft,GPIO.LOW)
            pwmLeft.start(speed)
            GPIO.output(directionRight,GPIO.HIGH)              #Left
            pwmRight.start(speed)

        elif event.value == 1:
            GPIO.output(directionLeft,GPIO.HIGH)
            pwmLeft.start(speed)
            GPIO.output(directionRight,GPIO.LOW)              #Right
            pwmRight.start(speed)

        elif event.value == 0:
            GPIO.output(directionLeft,GPIO.LOW)
            pwmLeft.stop()                                     #stop
            GPIO.output(directionRight,GPIO.LOW)
            pwmRight.stop()