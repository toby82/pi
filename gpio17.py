#!/usr/bin/python
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)
try:
	while True:
		GPIO.output(17,1)
		sleep(0.3)
		GPIO.output(17,0)
		sleep(0.3)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("done")
