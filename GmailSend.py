#!/usr/bin/env python

import smtplib
import sys
import argparse
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


def send(user, pwd, to, subject, text):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(user, pwd)
    mailServer.sendmail(user, to, msg.as_string())
    mailServer.close()


if __name__ == "__main__":
    desc = "To send emails from a gmail account.\n"
    desc += "\n"
    desc += "Example:\n"
    desc += "  ./GmailSend.py -u user@gmail.com -p password -t to@anywhere.com -s 'subject' -m 'message'\n"
    desc += "\n"
    desc += "or from another python script\n"
    desc += "  #!/usr/bin/env python\n"
    desc += "  import GmailSend\n"
    desc += "  GmailSend.send(user,password,to,subject,body)\n"

    epil = "Security Note:\n"
    epil += "  Passwords in scripts are stored in plan text.\n"
    epil += "  Passwords entered in the command line usually go into a bash_history file in plan text.\n"
    epil += "  Dont use a email account that you dont want compromised.\n"
    epil += "\n"

    parser = argparse.ArgumentParser(description=desc,
        epilog=epil,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument("-u", "--user", dest='user', required=True, help="The gmail account to send from")
    parser.add_argument("-p", "--password", dest='password', required=True)
    parser.add_argument("-t", "--to", dest="to", required=True)
    parser.add_argument("-s", "--subject", dest="subject", default="")
    parser.add_argument("-b", "--body", dest="body", default="")
    
    a = parser.parse_args()
    send(a.user, a.password, a.to, a.subject, a.body)
