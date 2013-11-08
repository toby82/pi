#!/usr/bin/python
#--------------------------------------   
#    ___                   ________    
#   / _ )___ __________ __/ ___/ (_)__ 
#  / _  / -_) __/ __/ // / /__/ / / _ \
# /____/\__/_/ /_/  \_, /\___/_/_/ .__/
#                  /___/        /_/  
#  
#       BerryClip - 6 LED Board
#
# This script turns on the buzzer
# useful for testing the buzzer
#
# Author : Matt Hawkins
# Date   : 12/11/2012
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import RPi.GPIO as GPIO
import time

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# Configure GPIO8 as an outout
GPIO.setup(8, GPIO.OUT)

# Turn Buzzer off
GPIO.output(8, False)

# Turn Buzzer on
GPIO.output(8, True)

# Wait 1 second
time.sleep(1)

# Turn Buzzer off
GPIO.output(8, False)

# Wait 1 second
time.sleep(1)

# Turn Buzzer on
GPIO.output(8, True)

# Wait 1 second
time.sleep(1)

# Turn Buzzer off
GPIO.output(8, False)

raw_input('The buzzer should have sounded twice, press enter to exit program')

# Reset GPIO settings
GPIO.cleanup()