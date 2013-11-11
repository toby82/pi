#!/usr/bin/python
import commands as cmd
import sys
import pdb
from time import sleep
import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText
mailto_list = ["toby82@139.com"]
mail_host = "mail.139.com"
mail_user = "toby82"
mail_pass = "775825811"
mail_postfix = "139.com"
content =""


class get_load_avg():
	#snmpcmd = 'snmpwalk -v 2c -c public 192.168.1.6 .1.3.6.1.4.1.2021.10.1.3'
	def __init__(self,snmpcmd):
		self.snmpcmd = snmpcmd
	def get_load_avg1(self):
		state,loadavg = cmd.getstatusoutput(self.snmpcmd)
		if state == 0:
			loadavg1 = loadavg.split('\n')[0].split()[3].replace('"','')
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		return loadavg1
	def get_load_avg5(self):
		state,loadavg = cmd.getstatusoutput(self.snmpcmd)
		if state == 0:
			loadavg5 = loadavg.split('\n')[1].split()[3].replace('"','')
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		return loadavg5
	def get_load_avg15(self):
		state,loadavg = cmd.getstatusoutput(self.snmpcmd)
		if state == 0:
			loadavg15 = loadavg.split('\n')[2].split()[3].replace('"','')
		else:
			print "snmpwalk error,exit."
			sys.exit(1)
		return loadavg15
	
	

def	blinkon(pin):
	GPIO.output(pin,GPIO.HIGH)
	
def blinkoff(pin):
	GPIO.output(pin,GPIO.LOW)

def	buzzeron(pin):
	GPIO.output(pin,GPIO.HIGH)
	
def buzzeroff(pin):
	GPIO.output(pin,GPIO.LOW)

def send_mail(to_list,sub,context):
    '''
    to_list:to_who
    sub:title
    content:content
    send_mail("xx@qq.com","sub","context")
    '''
    f_who = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    content ="This is test pi mail!"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = f_who
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(f_who,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False
'''    
if __name__ == "__main__":
    if send_mail(mailto_list,"pi mail test","content"):
        print "scucess"
    else:
        print "fails"
'''
	
try:
	pin = {'led1':17,'led2':21,'led3':22,'led4':23,'led5':24,'buzzer':25}
	GPIO.setmode(GPIO.BCM)
	for p in pin.itervalues():
		GPIO.setup(p,GPIO.OUT)
	#pdb.set_trace()
	snmpcmd = 'snmpwalk -v 2c -c public 192.168.7.45 .1.3.6.1.4.1.2021.10.1.3'
	avg = get_load_avg(snmpcmd)	
	while True:
		#print avg.get_load_avg1()
		if (0 <= float(avg.get_load_avg1()) <= 2):
			blinkon(pin[led1])
			blinkoff(pin[led2])
			blinkoff(pin[led3])
			blinkoff(pin[led4])
			blinkoff(pin[led5])
			buzzeroff(pin[buzzer])
			print "load average:0-2"
		elif (2 < float(avg.get_load_avg1()) <=4):
			blinkon(pin[led1])
			blinkon(pin[led2])
			blinkoff(pin[led3])
			blinkoff(pin[led4])
			blinkoff(pin[led5])
			buzzeroff(pin[buzzer])
			print "load average:2-4"
		elif (4 < float(avg.get_load_avg1()) <=6):
			blinkon(pin[led1])
			blinkon(pin[led2])
			blinkon(pin[led3])
			blinkoff(pin[led4])
			blinkoff(pin[led5])
			buzzeroff(pin[buzzer])
			print "load average:4-6"
		elif (6 < float(avg.get_load_avg1()) <=8):
			blinkon(pin[led1])
			blinkon(pin[led2])
			blinkon(pin[led3])
			blinkon(pin[led4])
			blinkoff(pin[led5])
			buzzeroff(pin[buzzer])
			print "load average:6-8"
		else:
			blinkon(pin[led1])
			blinkon(pin[led2])
			blinkon(pin[led3])
			blinkon(pin[led4])
			blinkon(pin[led5])
			buzzeron(pin[buzzer])
			sendmail()
			print "load average: > 8"
		#avg.get_load_avg5()
		#avg.get_load_avg15()
		print "*" * 50
		sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()


