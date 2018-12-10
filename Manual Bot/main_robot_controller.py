from __future__ import division
from evdev import InputDevice, categorize, ecodes, events
import Adafruit_PCA9685
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
gamepad = InputDevice('/dev/input/event0')
pwm = Adafruit_PCA9685.PCA9685()

angle1 = angle2 = angle3 = 400
speed = 50           # pwm to motors
steps = 25           # servo steps  = 25 * ( 180 / 500 ) 
stepper_steps = 25   # stepper steps = ( 360 / 200 ) * 25

Arm = False
Motor = True

GPIO.setwarnings(False)

SuctionPin = 21 
directionLeft = 17              #physical 11
directionRight = 27             #physical 13
GPIO.setup(directionLeft,GPIO.OUT)
GPIO.setup(directionRight,GPIO.OUT)

GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(SuctionPin,GPIO.OUT)

pwmLeft = GPIO.PWM(15, 1000)    #physical 10
pwmRight = GPIO.PWM(18, 1000)   #physical 12

DIR = 20
STEP = 21
CW = 1
CCW = 0
SPR = 200
delay = .005
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

pwm.set_pwm(2, 0, 400 )
time.sleep(2)
pwm.set_pwm(3, 0, 400 )
time.sleep(2)
pwm.set_pwm(4, 0, 300 )
time.sleep(2)

def drive():

    global Motor, Arm, gamepad, pwmLeft, directionLeft, pwmRight, directionRight, speed
    print("Entered 1")
    for event in gamepad.read_loop():

        if event.code == 17:

            if event.value == -1:
                GPIO.output(directionLeft,GPIO.LOW)
                pwmLeft.start(speed)
                GPIO.output(directionRight,GPIO.HIGH)              #Forward
                pwmRight.start(speed)
        
            elif event.value == 1:
                GPIO.output(directionLeft,GPIO.HIGH)
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
                GPIO.output(directionLeft,GPIO.HIGH)
                pwmLeft.start(speed)
                GPIO.output(directionRight,GPIO.HIGH)              #Left
                pwmRight.start(speed)

            elif event.value == 1:
                GPIO.output(directionLeft,GPIO.LOW)
                pwmLeft.start(speed)
                GPIO.output(directionRight,GPIO.LOW)              #Right
                pwmRight.start(speed)

            elif event.value == 0:
                GPIO.output(directionLeft,GPIO.LOW)
                pwmLeft.stop()                                     #stop
                GPIO.output(directionRight,GPIO.LOW)
                pwmRight.stop()

        elif event.code == 312:
            if event.value == 1:
                Arm = True
                Motor = False
                print("Arm Mode")
                break;

def arm():

    global gamepad, Motor, Arm, angle1, angle2, angle3, pwm, DIR, CW, CCW, SPR, delay,STEP, steps, SuctionPin
    print("Entered 2")
    for event in gamepad.read_loop():

        if event.code == 17:

            if event.value == -1:
                GPIO.output(SuctionPin,GPIO.HIGH)               #Suction On

            elif event.value == 1:
                GPIO.output(SuctionPin,GPIO.LOW)               #Sunction Off

        elif event.code == 16:

            if event.value == -1:
                pwm.set_pwm(1, 0, 150 )                     #Dart Released
            elif event.value == 1:
                pwm.set_pwm(1, 0, 650 )

        if event.code == 304:

            if event.value == 0 :
                angle1 = angle1 + steps
                if angle1>=650:
                    angle1 = 650
                pwm.set_pwm(2, 0, angle1)
                time.sleep(0.5)

	if event.code == 306:
		if event.value == 1:
        	        angle1 = angle1 - steps
                	if angle1<150:
                    		angle1 = 150
               		pwm.set_pwm(2, 0, angle1)
                	time.sleep(0.2)
        
        if event.code == 307:

            if event.value == 1:
                angle2 = angle2 + steps
                if angle2>=650:
                    angle2 = 650
                pwm.set_pwm(3, 0, angle2)
                time.sleep(0.2)

        if event.code == 305:

            if event.value == 1:
                angle2 = angle2 - steps
                if angle2<150:
                    angle2 = 150
                pwm.set_pwm(3, 0, angle2)
                time.sleep(0.2)
        
        if event.code == 310:
        
            if event.value == 1:
                angle3 = angle3 + 50
                if angle1>=650:
                    angle3 = 650
                pwm.set_pwm(4, 0, angle3)
                time.sleep(0.2)
                print("base motor +")
        
        if event.code == 311:
        
            if event.value == 1:
                angle3 = angle3 - 50
                if angle3<150:
                    angle3 = 150
                pwm.set_pwm(4, 0, angle3)
                time.sleep(0.2)
                print("base motor -")
        
        if event.code == 309:
        
            if event.value == 1:
                GPIO.output(DIR, CW)
    
                for x in range(stepper_steps):
                    GPIO.output(STEP, GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(STEP, GPIO.LOW)
    
        if event.code == 308:
            if event.value == 1:
                GPIO.output(DIR, CCW)

                for x in range(stepper_steps):
                    GPIO.output(STEP, GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(STEP, GPIO.LOW)
                    sleep(delay)

        if event.code == 313:
            
            if event.value == 1:
                Motor = True
                Arm = False
                print("Drive Mode")
                break


def main():

    global Arm , Motor

    while True:
        if Arm == True:
            arm()
        elif Motor == True:
            drive()

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting Down")
    finally:
        GPIO.cleanup()
