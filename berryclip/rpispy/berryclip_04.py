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
# This script lights the 6 LEDs in sequence
# when the switch is pressed.
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

# Set LED GPIO pins as outputs
GPIO.setup(4 , GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9 , GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

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

    # Turn off LEDs
    GPIO.output(4 , False)
    GPIO.output(17, False)
    GPIO.output(22, False)
    GPIO.output(10, False)
    GPIO.output(9 , False)
    GPIO.output(11, False)
   
    if GPIO.input(7)==1:
      print "  Button pressed!"
        
      # Turn off LEDs
      GPIO.output(4 , False)
      GPIO.output(17, False)
      GPIO.output(22, False)
      GPIO.output(10, False)
      GPIO.output(9 , False)
      GPIO.output(11, False)
        
      # Turn on LEDs in sequence
      GPIO.output(4 , True)
      time.sleep(0.5)
      GPIO.output(17, True)
      time.sleep(0.5)
      GPIO.output(22, True)
      time.sleep(0.5)
      GPIO.output(10, True)
      time.sleep(0.5)
      GPIO.output(9 , True)
      time.sleep(0.5)
      GPIO.output(11, True)
      
      # Wait 2 seconds
      time.sleep(2)
      
      print "Press the button (CTRL-C to exit)"
      
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()