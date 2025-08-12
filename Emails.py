#smtplib is the library
#smtp means simple mail transfer protocol
#getpass loibrary used to get an information in hidden way like passwords
import smtplib
import getpass
smtp_obj = smtplib.SMTP('smtp.gmail.com',587)#smtp server , port number
smtp_obj.ehlo() #to connect with smtp server
smtp_obj.starttls() #encryption
password = getpass.getpass('Password Please:')
email = getpass.getpass('Email')
#generate an app password that telss the smtp servere like gmail to knoe
#there is a script going to hit.
smtp_obj.login(email,password)
from_address = email
to_address = email
subject = input("enter subject")
message = input("eneter message")
msg = "Subject: "+ subject + '\n' + message #the function accepts one string so to differentiate between body and sub
smtp_obj.sendmail(from_address,to_address,msg)
#a successful completion of this function return {} empty dictionary.
#impalib required for viewing mail inbox

