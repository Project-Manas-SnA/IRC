from __future__ import division
from evdev import InputDevice, categorize, ecodes, events
import Adafruit_PCA9685
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
gamepad = InputDevice('/dev/input/event17')
pwm = Adafruit_PCA9685.PCA9685()
ARM = False
Motor = True
servo1 = servo2 = servo3 = 400

speed = 50           # pwm to motors
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


pwmLeft = GPIO.PWM(15, 1000)    #physical 10
directionLeft = 17              #physical 11
pwmRight = GPIO.PWM(18, 1000)   #physical 12
directionRight = 27             #physical 13

GPIO.setup(directionLeft,GPIO.OUT)
GPIO.setup(pwmLeft,GPIO.OUT)

GPIO.setup(directionRight,GPIO.OUT)
GPIO.setup(pwmRight,GPIO.OUT)


for i in range(150, 400, 50):
    pwm.set_pwm(0, 0, i)
    time.sleep(0.5)

for i in range(150, 400, 50):
    pwm.set_pwm(1, 0, i)
    time.sleep(0.5)

for i in range(150, 400, 50):
    pwm.set_pwm(2, 0, i)
    time.sleep(0.5)

def drive():

    global ARM, gamepad, pwmLeft, directionLeft, pwmRight, directionRight, speed

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
        elif event.code == 4:
            if event.vaue == 589833:
                ARM = True
                Motor = False
                break;

def arm():

    global gamepad, Motor, servo1, servo2, servo3, pwm, DIR, CW, CCW, SPR, delay,STEP, steps

    for event in gamepad.read_loop():

        if event.code == 04:

            if event.value == 589825 :
                servo1 = servo1 + steps
                if servo1>=650:
                    servo1 = 650
                pwm.set_pwm(0, 0, servo1)
                time.sleep(0.5)

            if event.value == 589827:
                servo1 = servo1 - steps
                if servo1<150:
                    servo1 = 150
                pwm.set_pwm(0, 0, servo1)
                time.sleep(0.5)

            if event.value == 589828:
                servo2 = servo2 + steps
                if servo2>=650:
                    servo2 = 650
                pwm.set_pwm(1, 0, servo2)
                time.sleep(0.5)

            if event.value == 589826:
                servo2 = servo2 - steps
                if servo2<150:
                    servo2 = 150
                pwm.set_pwm(1, 0, servo2)
                time.sleep(0.5)

            if event.value == 589831:
                servo3 = servo3 + steps
                if servo1>=650:
                    servo3 = 650
                pwm.set_pwm(2, 0, servo1)
                time.sleep(0.5)

            if event.value == 589832:
                servo3 = servo3 - steps
                if servo3<150:
                    servo3 = 150
                pwm.set_pwm(2, 0, servo3)
                time.sleep(0.5)

                if event.value == 589830:
                    GPIO.output(DIR, CW)

                    for x in range(stepper_steps):
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)

                if event.value == 589829:
                    GPIO.output(DIR, CCW)

                    for x in range(stepper_steps):
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)


            if event.value == 589834:
                Motor = True
                Arm = False
                break

def main():

    global ARM , Motor

    while True:
        if ARM == True:
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
