from __future__ import division
from evdev import InputDevice, categorize, ecodes, events
import Adafruit_PCA9685
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
gamepad = InputDevice('/dev/input/event17')
pwm = Adafruit_PCA9685.PCA9685()

pwmLeft = GPIO.PWM(15, 1000)    #physical 10
directionLeft = 17              #physical 11
pwmRight = GPIO.PWM(18, 1000)   #physical 12
directionRight = 27             #physical 13

1A = 6
1B = 13
1C = 19

2A = 16
2B = 20
2E = 21
GPIO.setup(1A,GPIO.OUT)
GPIO.setup(1B,GPIO.OUT)
GPIO.setup(1E,GPIO.OUT)

GPIO.setup(2A,GPIO.OUT)
GPIO.setup(2B,GPIO.OUT)
GPIO.setup(2E,GPIO.OUT)

GPIO.setup(directionLeft,GPIO.OUT)
GPIO.setup(pwmLeft,GPIO.OUT)

GPIO.setup(directionRight,GPIO.OUT)
GPIO.setup(pwmRight,GPIO.OUT)

servo1 = 400
servo2 = 400
servo3 = 400

for i in range(150, 650, 50):
    pwm.set_pwm(0, 0, i)
    time.sleep(0.5)

for i in range(150, 650, 50):
    pwm.set_pwm(1, 0, i)
    time.sleep(0.5)

for i in range(150, 650, 50):
    pwm.set_pwm(2, 0, i)
    time.sleep(0.5)

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

    elif event.code == 04:

        if event.value == 589825 :
            servo1 = servo1 + 25
            if servo1>=650:
                servo1 = 650
            pwm.set_pwm(0, 0, servo1)
            time.sleep(0.5)

        if event.value == 589827:
            servo1 = servo1 - 25
            if servo1<150:
                servo1 = 150
            pwm.set_pwm(0, 0, servo1)
            time.sleep(0.5)

        if event.value == 589828:
            servo2 = servo2 + 25
            if servo2>=650:
                servo2 = 650
            pwm.set_pwm(1, 0, servo2)
            time.sleep(0.5)

        if event.value == 589826:
            servo2 = servo2 - 25
            if servo2<150:
                servo2 = 150
            pwm.set_pwm(1, 0, servo2)
            time.sleep(0.5)

        if event.value == 589831:
            servo3 = servo3 + 25
            if servo1>=650:
                servo3 = 650
            pwm.set_pwm(2, 0, servo1)
            time.sleep(0.5)

        if event.value == 589832:
            servo3 = servo3 - 25
            if servo3<150:
                servo3 = 150
            pwm.set_pwm(2, 0, servo3)
            time.sleep(0.5)

    if event.code == 16:

        if event.value == 1:
            GPIO.output(1A,GPIO.HIGH)
            GPIO.output(1B,GPIO.HIGH)
            GPIO.output(1E,GPIO.HIGH)

            GPIO.output(2A,GPIO.LOW)
            GPIO.output(2B,GPIO.LOW)
            GPIO.output(2E,GPIO.LOW)
            time.sleep(0.5)

        if event.value == 0
            GPIO.output(1A,GPIO.LOW)
            GPIO.output(1B,GPIO.LOW)
            GPIO.output(1E,GPIO.LOW)

            GPIO.output(2A,GPIO.LOW)
            GPIO.output(2B,GPIO.LOW)
            GPIO.output(2E,GPIO.LOW)
            time.sleep(0.5)

        if event.code == -1:
            GPIO.output(2A,GPIO.HIGH)
            GPIO.output(2B,GPIO.HIGH)
            GPIO.output(2E,GPIO.HIGH)

            GPIO.output(1A,GPIO.LOW)
            GPIO.output(1B,GPIO.LOW)
            GPIO.output(1E,GPIO.LOW)
            time.sleep(0.5)

        if event.value == 0
            GPIO.output(1A,GPIO.LOW)
            GPIO.output(1B,GPIO.LOW)
            GPIO.output(1E,GPIO.LOW)

            GPIO.output(2A,GPIO.LOW)
            GPIO.output(2B,GPIO.LOW)
            GPIO.output(2E,GPIO.LOW)
            time.sleep(0.5)
