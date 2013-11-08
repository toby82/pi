#!/usr/bin/python
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO")
from time import sleep
led_port_list = [17]
def led_init():
	GPIO.setmode(GPIO.BCM)
	for port in led_port_list:
		GPIO.setup(port,GPIO.OUT,initial=GPIO.LOW)

def led_start():
	while True:
		for port in led_port_list:
			GPIO.output(port,True)
			sleep(1)
			GPIO.output(port,False)


if __name__ == '__main__':
	led_init()
	led_start()
