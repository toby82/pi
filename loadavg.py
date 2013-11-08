#!/usr/bin/python
import sys
import os
from time import sleep
import commands as cmd
sys.path.append('/root/pi/pi')
import led02
snmpcmd = 'snmpwalk -v 2c -c public 192.168.1.6 .1.3.6.1.4.1.2021.10.1.3'
while True:
	v1 = led02.get_load_avg(snmpcmd)
	v11 = v1.get_load_avg1()
	print v11
	if float(v11) > float(6):
		sleep(10)
		os.system('killall yes')
		break
	else:
		os.system('yes > /dev/null &')
	sleep(2)
#	print load1
