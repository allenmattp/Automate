import imapclient, passwordGen, pyzmail, subprocess
from datetime import datetime

# grab my app password so I don't upload it to github
password = passwordGen.passGen()

# sign into IMAP server
conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conn.login("allenmattpdev@gmail.com", password)

# only need to look at recent emails, so create variable for today's date
today = datetime.date(datetime.today())

conn.select_folder("INBOX", readonly=False)
UIDs = conn.search(["SINCE", today])
print(UIDs)

for i in range(len(UIDs)):
    rawMessage = conn.fetch([UIDs[i]], ["BODY[]", "FLAGS"])
    marker = UIDs[i]
    message = pyzmail.PyzMessage.factory(rawMessage[marker][b"BODY[]"])
    if message.get_subject() == "Execute Order":    # Look for this phrase
        body = message.text_part.get_payload().decode(message.text_part.charset)
        if body.find("password"):                   # For security... include a password in the body of email
            subprocess.Popen("C:\\Users\\Wizard\\PycharmProjects\\bat files\\rainCheck.bat") # some process

        conn.delete_messages([UIDs[i]])   # Delete message so it doesn't trigger on next check
        conn.expunge()


conn.logout()