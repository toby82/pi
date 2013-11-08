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
# This script tests the switch.
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

print "Setup GPIO pins as inputs and outputs"

# Set Switch GPIO as input
GPIO.setup(7 , GPIO.IN)

print "Press the button"

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  # Loop until users quits with CTRL-C
  while True :
   
    if GPIO.input(7)==1:
      print "  Button pressed!"
      time.sleep(0.5)
      print "Press the button (CTRL-C to exit)"
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()