from email.header import Header
from email.mime.text import MIMEText
#from getpass import getpass
from smtplib import SMTP_SSL
import random

login = "jaideeprda@gmail.com"
password = ""

recipients = ["jaideepsaini3460@gmail.com"]

msg = MIMEText("we are lerning python")
msg ['subject'] = Header('equction')
msg ['from'] = login
msg ['To'] = ", ".join(recipients)

s =  SMTP_SSL("smtp.gmail.com' 465,timeout=10")
s.set_debuglevel(1)
try:
    s.login(login,password)
    s.sendmail(msg['from'],recipients, msg.as_string())

finally:
    s.quit()

#s = SMTP_SSL('smtp.gmail.com ' 465,timeout=10)

















#jaideep saini is best coder for python developer

