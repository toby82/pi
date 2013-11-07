#!/usr/bin/python
import commands as cmd
import sys
from time import sleep
def get_load_avg():
	while True:
		state,loadavg = cmd.getstatusoutput('snmpwalk -v 2c -c public 192.168.1.6 .1.3.6.1.4.1.2021.10.1.3')
		if state == 0:
			loadavg1 = loadavg.split('\n')[0].split()[3].replace('"','')
			loadavg5 = loadavg.split('\n')[1].split()[3].replace('"','')
			loadavg15 = loadavg.split('\n')[2].split()[3].replace('"','')
			print loadavg1
			print loadavg5
			print loadavg15
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		sleep(5)


try:
	get_load_avg()
except KeyboardInterrupt:
	pass
