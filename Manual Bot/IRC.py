from __future__ import division
from evdev import InputDevice, categorize, ecodes, events
import Adafruit_PCA9685
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
gamepad = InputDevice('/dev/input/event9')
pwm = Adafruit_PCA9685.PCA9685()


MotorLA = 16
MotorLB = 18

MotorRA = 23
MotorRB = 21

GPIO.setup(MotorLA,GPIO.OUT)
GPIO.setup(MotorLB,GPIO.OUT)

GPIO.setup(MotorRA,GPIO.OUT)
GPIO.setup(MotorRB,GPIO.OUT)


for event in gamepad.read_loop():
    if event.code == 17:
        if event.value == -1:
            GPIO.output(MotorLA,GPIO.HIGH)
            GPIO.output(MotorLB,GPIO.LOW)
            GPIO.output(MotorRA,GPIO.HIGH)              #Forward
            GPIO.output(MotorRB,GPIO.LOW)

            break

        if event.value == 1:
            GPIO.output(MotorLA,GPIO.LOW)
            GPIO.output(MotorLB,GPIO.HIGH)
            GPIO.output(MotorRA,GPIO.LOW)
            GPIO.output(MotorRB,GPIO.HIGH)
            break

    elif event.code == 16:

        if event.value == -1:
            GPIO.output(MotorLA,GPIO.LOW)
            GPIO.output(MotorLB,GPIO.HIGH)
            GPIO.output(MotorRA,GPIO.HIGH)              #Left
            GPIO.output(MotorRB,GPIO.LOW)
            break

        if event.value == 1:
            GPIO.output(MotorLA,GPIO.HIGH)
            GPIO.output(MotorLB,GPIO.LOW)
            GPIO.output(MotorRA,GPIO.LOW)              #Right
            GPIO.output(MotorRB,GPIO.HIGH)



pwm.set_pwm(0, 0, 400)
time.sleep(1)

pwm.set_pwm(1, 0, 400)
time.sleep(1)

pwm.set_pwm(2, 0, 400)
time.sleep(1)

