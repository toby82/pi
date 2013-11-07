#!/usr/bin/python
import commands as cmd
import sys
from time import sleep
class get_load_avg():
	#ip = '192.168.1.6'
	#snmpcmd = 'snmpwalk -v 2c -c public 192.168.1.6 .1.3.6.1.4.1.2021.10.1.3'
	def __init__(self,arg):
		self.snmpcmd = arg
	def get_load_avg1(self):
		state,loadavg = cmd.getstatusoutput(self.snmpcmd)
		if state == 0:
			loadavg1 = loadavg.split('\n')[0].split()[3].replace('"','')
				#loadavg5 = loadavg.split('\n')[1].split()[3].replace('"','')
				#loadavg15 = loadavg.split('\n')[2].split()[3].replace('"','')
			print loadavg1
				#print loadavg5
				#print loadavg15
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		return loadavg1
	def get_load_avg5(self):
		state,loadavg = cmd.getstatusoutput(self.snmpcmd)
		if state == 0:
			#loadavg5 = loadavg.split('\n')[0].split()[3].replace('"','')
			loadavg5 = loadavg.split('\n')[1].split()[3].replace('"','')
				#loadavg15 = loadavg.split('\n')[2].split()[3].replace('"','')
			print loadavg5
				#print loadavg5
				#print loadavg15
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		return loadavg5
	def get_load_avg15(self):
		state,loadavg = cmd.getstatusoutput(self.snmpcmd)
		if state == 0:
			#loadavg5 = loadavg.split('\n')[0].split()[3].replace('"','')
			#loadavg5 = loadavg.split('\n')[1].split()[3].replace('"','')
			loadavg15 = loadavg.split('\n')[2].split()[3].replace('"','')
			print loadavg15
				#print loadavg5
				#print loadavg15
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		return loadavg15
			
try:
	snmpcmd = 'snmpwalk -v 2c -c public 192.168.1.6 .1.3.6.1.4.1.2021.10.1.3'
	avg = get_load_avg(snmpcmd)	
	while True:
		avg.get_load_avg1()
		avg.get_load_avg5()
		avg.get_load_avg15()
		print "*" * 50
		sleep(5)
except KeyboardInterrupt:
	pass
