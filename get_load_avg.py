#!/usr/bin/python
import commands as cmd
import sys
from time import sleep
class get_load_avg():
	#snmpcmd = 'snmpwalk -v 2c -c public 192.168.1.6 .1.3.6.1.4.1.2021.10.1.3'
	def __init__(self,snmpcmd):
		self.snmpcmd = snmpcmd
	def get_load_avg1(self):
		state,loadavg = cmd.getstatusoutput(self.snmpcmd)
		if state == 0:
			loadavg1 = loadavg.split('\n')[0].split()[3].replace('"','')
				#loadavg5 = loadavg.split('\n')[1].split()[3].replace('"','')
				#loadavg15 = loadavg.split('\n')[2].split()[3].replace('"','')
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		return loadavg1
	def get_load_avg5(self):
		state,loadavg = cmd.getstatusoutput(snmpcmd)
		if state == 0:
			#loadavg5 = loadavg.split('\n')[0].split()[3].replace('"','')
			loadavg5 = loadavg.split('\n')[1].split()[3].replace('"','')
				#loadavg15 = loadavg.split('\n')[2].split()[3].replace('"','')
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		return loadavg5
	def get_load_avg15(self):
		state,loadavg = cmd.getstatusoutput(snmpcmd)
		if state == 0:
			#loadavg5 = loadavg.split('\n')[0].split()[3].replace('"','')
			#loadavg5 = loadavg.split('\n')[1].split()[3].replace('"','')
			loadavg15 = loadavg.split('\n')[2].split()[3].replace('"','')
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		return loadavg15
			
