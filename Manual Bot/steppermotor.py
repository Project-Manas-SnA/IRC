import time
import RPi.GPIO as GPIO

steps = 25           # servo steps  = 25 * ( 180 / 500 ) 
stepper_steps = 25   # stepper steps = ( 360 / 200 ) * 25

DIR = 20
STEP = 21
CW = 1
CCW = 0
SPR = 200
delay = .005
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.output(DIR, CCW)
for x in range(stepper_steps):
	GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

GPIO.output(DIR, CW)
for x in range(stepper_steps):
	GPIO.output(STEP, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	time.sleep(delay)