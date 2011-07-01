GmailSend
========
Send email messages from the command line using a gmail account. Intended for automated notification from scripts.

Example
--------

	./GmailSend.py -u user@gmail.com -p password -t to@anywhere.com -s 'subject' -m 'message'

or from another python script

	#!/usr/bin/env python
	import GmailSend
	GmailSend.send(user,password,to,subject,body)

Usage
--------
	usage: GmailSend.py [-h] -u USER -p PASSWORD -t TO [-s SUBJECT] [-b BODY]

	To send emails from a gmail account.

	optional arguments:
	  -h, --help            show this help message and exit
	  -u USER, --user USER  The gmail account to send from
	  -p PASSWORD, --password PASSWORD
	  -t TO, --to TO
	  -s SUBJECT, --subject SUBJECT
	  -b BODY, --body BODY
	
	Security Note:
	  Passwords in scripts are stored in plan text.
	  Passwords entered in the command line usually go into a bash_history file in plan text.
	  Dont use a email account that you dont want compromised.
