#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText
mailto_list = ["toby82@139.com"]
mail_host = "mail.139.com"
mail_user = "toby82"
mail_pass = "775825811"
mail_postfix = "139.com"
content ="this is test mail!"

def send_mail(to_list,sub,context):
    '''
    to_list:to_who
    sub:title
    content:content
    send_mail("xx@qq.com","sub","context")
    '''
    f_who = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
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
    
if __name__ == "__main__":
    if send_mail(mailto_list,"pi mail test","content"):
        print "scucess"
    else:
        print "fails"