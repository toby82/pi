#!/usr/bin/python
#--------------------------------------   
#    ___                   ________    
#   / _ )___ __________ __/ ___/ (_)__ 
#  / _  / -_) __/ __/ // / /__/ / / _ \
# /____/\__/_/ /_/  \_, /\___/_/_/ .__/
#                  /___/        /_/  
#  
#       Battery Uptime Test
#
# This script lights the 6 LEDs in
# sequence, 1 LED at a time while
# printing out the time the script has
# been running. Used for testing the
# runtime of battery packs.
#
# Author : Matt Hawkins
# Date   : 14/10/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#-------------------------------------- 

# Import required libraries
import RPi.GPIO as GPIO
import sys
import time
import datetime

start = datetime.datetime.now()

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

# List of LED GPIO numbers
LedSeq = [4,17,22,10,9,11]

# Get delay from command line or set default
if len(sys.argv)==2:
  delay = float(sys.argv[1])
else:
  delay = 0.1

# Set up the GPIO pins as outputs and set False
print "Setup Outputs"
for x in range(6):
  GPIO.setup(LedSeq[x], GPIO.OUT)
  GPIO.output(LedSeq[x], False)

# Set step size and direction
step=1

seq_count=0

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  # Loop until users quits with CTRL-C
  while True:

    # Loop through sequence 0 to 9
    # and 9 to 0  
    while seq_count<6 and seq_count>=0:
      # Delay
      time.sleep(delay)
      # Loop through each LED
      for y in range(6) :
        if y==seq_count :
          # This LED is ON
          GPIO.output(LedSeq[y], True)
        else:
          # This LED is OFF
          GPIO.output(LedSeq[y], False)

      # Move the sequence one step
      seq_count += step
    
    # Invert the step so sequence runs
    # in opposite direction
    step = step * -1

    # Correct sequence count by 2 steps
    seq_count=seq_count + step + step
    
    uptime = datetime.datetime.now() - start
    
    print uptime
    
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()