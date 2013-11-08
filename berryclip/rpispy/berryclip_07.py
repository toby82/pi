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
# This script simulates a dice throw.
# Press the button and a random number
# of LEDs are turned on.
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
import random

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# List of LED GPIO numbers
LedSeq = [4,17,22,10,9,11]

# Set up the GPIO pins as outputs and set False
print "Setup LED pins as outputs"
for x in range(6):
  GPIO.setup(LedSeq[x], GPIO.OUT)
  GPIO.output(LedSeq[x], False)

# Switch on GPIO7
print "Setup Switch pin as input"
GPIO.setup(7, GPIO.IN)

random.seed()

print "Press the button to roll the dice (CTRL-C to exit)"

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  # Loop until users quits with CTRL-C
  while True :

    if GPIO.input(7)==1:
      
      # Turn off all 6 LEDs
      for x in range(6):
        GPIO.output(LedSeq[x], False)      

      time.sleep(0.5)
        
      # Roll dice
      result = random.randint(1,6)
      
      print "You rolled a " + str(result)

      # Turn on LEDs
      for x in range(result):
        GPIO.output(LedSeq[x], True)  
        
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()