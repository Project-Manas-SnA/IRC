import time
import RPi.GPIO as GPIO

SuctionPin = 2 
GPIO.setup(SuctionPin,GPIO.OUT)

while true:
	GPIO.output(SuctionPin,GPIO.HIGH)  
	time.sleep(1)
	GPIO.output(SuctionPin,GPIO.LOW)
	time.sleep  