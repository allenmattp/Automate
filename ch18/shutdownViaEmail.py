#! python3
# shutdownViaEmail.py - Send an email to shutdown your computer.

import imapclient, passwordGen, pyzmail, subprocess, os
from datetime import datetime

# grab password from somewhere else so it's not uploaded it to github
password = passwordGen.passGen()

# sign into IMAP server
conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conn.login("allenmattpdev@gmail.com", password)

# only want to check recent emails, so create a variable for today's date
today = datetime.date(datetime.today())

conn.select_folder("INBOX", readonly=False)         # CAUTION: readonly=False
UIDs = conn.search(["SINCE", today])

# Search through all of today's emails in inbox
for i in range(len(UIDs)):
    rawMessage = conn.fetch([UIDs[i]], ["BODY[]", "FLAGS"])
    marker = UIDs[i]
    message = pyzmail.PyzMessage.factory(rawMessage[marker][b"BODY[]"])

    # check subject line for trigger phrase
    if message.get_subject() == "Shutdown Sequence":
        body = message.text_part.get_payload().decode(message.text_part.charset)

        # check for secret password and, if found, run some process
        if body.find("Initialize"):
            # Delete message so it doesn't trigger on next check
            conn.delete_messages([UIDs[i]])
            conn.expunge()

            # shutdown
            os.system("shutdown /s")



conn.logout()