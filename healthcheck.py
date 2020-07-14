import commands
import re
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_mail(send_from, send_to, subject, message,
              server, port, username, password,
              use_tls):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

def main():

    test = commands.getstatusoutput("""cvpi status all""")
    
    if "failed" in str(test):
        print "At least one service failed in the cluster"
        send_from = "sender@domain.com"
        send_to = ["receiver@domain.com"]
        subject = "CVP Health Problem"
        message = "At least one service failed in the cluster"
        server = "smtp.domain.com"
        username = "username"
        password = "password"
        port =587
        use_tls = True
        send_mail(send_from, send_to, subject, message, server, port, username, password, use_tls )

if __name__ == '__main__':
    main()
