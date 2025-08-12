
import os
from imbox import Imbox  # pip install imbox
import traceback
import datetime

# enable less secure apps on your google account
# https://myaccount.google.com/lesssecureapps

host = "imap.gmail.com"
username = "kartu621@gmail.com"
password = 'arnl uhbb ewyg ynia'
#download_folder = "/path/to/download/folder"

#if not os.path.isdir(download_folder):
    #os.makedirs(download_folder, exist_ok=True)

mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(date__lt=datetime.date(2024, 7, 4),date__gt=datetime.date(2024, 7, 3))  # defaults to inbox //year month day
for (uid, message) in messages:
    #mail.mark_seen(uid)
    print(message.sent_from)
    print(message.date)
    print(message.body)
    # optional, mark message as read



mail.logout()
#https://pypi.org/project/imbox/