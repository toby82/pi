#!/usr/bin/python
import RPi.GPIO as GPIO
import time
# Define GPIO pins
OUTPUTS = { 'led0':4,'led1':17,'led2':27,'led3':22,'led4':10,'led5':9,'led6':8}
#OUTPUTS = { 'led1':17,'led2':27,'led3':22,'led4':10,'led5':9,'led6':11,'buzzer':8 }
INPUTS  = { 'switch1':7,'tmp':18 }
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
try:
	while True:
		for pin in OUTPUTS.values():
			GPIO.setup(pin,GPIO.OUT)
		for pin in INPUTS.values():
			GPIO.setup(pin,GPIO.IN)
		for pin in OUTPUTS.values():
			GPIO.output(pin,GPIO.HIGH)
			time.sleep(0.1)
	#time.sleep1)
		for pin in OUTPUTS.values():
			GPIO.output(pin,GPIO.LOW)
			time.sleep(0.1)
except KeyboardInterrupt:
	print "Goodbye!"
	GPIO.cleanup()
