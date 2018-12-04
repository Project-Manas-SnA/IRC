import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 1000)

p.start(7.5)

try:
    for i in range(0,200,1):
	j = i/2 +0.5
        p.ChangeDutyCycle(j) # turn towards 90 degree
        time.sleep(1)
	print(j)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

