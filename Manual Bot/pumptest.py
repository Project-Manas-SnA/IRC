import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

SuctionPin = 17
GPIO.setup(SuctionPin,GPIO.OUT)


while True:
	GPIO.output(SuctionPin,GPIO.HIGH)
	time.sleep(10)
	print("on")
	GPIO.output(SuctionPin,GPIO.LOW)
	time.sleep(10)
	print("off")
