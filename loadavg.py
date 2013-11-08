#!/usr/bin/python
import sys
import os
from time import sleep
import commands as cmd
sys.path.append('/root/pi/pi')
import get_load_avg
snmpcmd = 'snmpwalk -v 2c -c public 192.168.1.6 .1.3.6.1.4.1.2021.10.1.3'
while True:
	ins_get = get_load_avg.get_load_avg(snmpcmd)
	ins_getavg = v1.get_load_avg1()
	print ins_getavg
	if float(ins_getavg) > float(6):
		sleep(10)
		os.system('killall yes')
		break
	else:
		os.system('yes > /dev/null &')
	sleep(2)
#	print load1
