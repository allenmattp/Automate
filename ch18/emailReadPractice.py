import imapclient, passwordGen, datetime, pyzmail

# grab my app password so I don't upload it to github
password = passwordGen.passGen()

# sign into IMAP server
conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conn.login("allenmattpdev@gmail.com", password)


conn.select_folder("INBOX", readonly=True)
UIDs = conn.search(["SINCE", datetime.date(2021, 1, 1)])
print(UIDs)

for i in range(len(UIDs)):
    rawMessage = conn.fetch([UIDs[i]], ["BODY[]", "FLAGS"])
    marker = UIDs[i]
    message = pyzmail.PyzMessage.factory(rawMessage[marker][b"BODY[]"])
    print(message.get_subject())
    if message.text_part:
        print(message.text_part.get_payload().decode(message.text_part.charset))

"""rawMessages = conn.fetch([UIDs[0]], ["BODY[]", "FLAGS"])
print(rawMessages)

message = pyzmail.PyzMessage.factory(rawMessages[3][b"BODY[]"])

print(message.get_subject())
print(message.get_addresses("to"))

if message.text_part:
    print(message.text_part.get_payload().decode(message.text_part.charset))"""

conn.logout()