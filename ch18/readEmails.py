import imapclient, passwordGen, datetime, pyzmail, pprint, imaplib

# increase size limit
imaplib._MAXLINE = 10000000

# grab my app password so I don't upload it to github
password = passwordGen.passGen()

# sign into IMAP server
conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conn.login("allenmattpdev@gmail.com", password)

# get folders
folders = conn.list_folders()
# return numbered list of all folders
print("Available folders:")
for count, folder in enumerate(folders, start=1):
    print(f"{count}. {folder[2]}")

# user enters number to select a folder
folderSelect = int(input("\nEnter folder number: ")) - 1
conn.select_folder(folders[folderSelect][2], readonly=True)

# fetch ALL emails from selected folder
UIDs = conn.search(["ALL"])
print(UIDs)

# print out email subject and body
for i in range(len(UIDs)):
    rawMessage = conn.fetch([UIDs[i]], ["BODY[]", "FLAGS"])
    marker = UIDs[i]
    message = pyzmail.PyzMessage.factory(rawMessage[marker][b"BODY[]"])
    print(message.get_addresses("from"))
    print(message.get_subject())
    if message.text_part is not None:
        print(message.text_part.get_payload().decode(message.text_part.charset))
    if message.html_part is not None:
        print(message.html_part.get_payload().decode(message.html_part.charset))
    print("\n\n***** NEW MESSAGE *****\n\n")

# logout
conn.logout()