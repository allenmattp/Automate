#! python3
# unsubscribeSearch.py - searches for Unsubscribe link in specified gmail folder and opens link.


import imapclient, datetime, pyzmail, pprint, imaplib, bs4, webbrowser

# increase size limit
imaplib._MAXLINE = 10000000

# enter credentials (gmail must have less secure apps unblocked)
username = input("Enter gmail: ")
password = input("Enter password: ")

# sign into IMAP server
conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conn.login(username, password)

# get folders
folders = conn.list_folders()
# return numbered list of all folders
print("Available folders:")
for count, folder in enumerate(folders, start=1):
    print(f"{count}. {folder[2]}")

# user enters number to select a folder
folderSelect = int(input("\nEnter folder number: ")) - 1
conn.select_folder(folders[folderSelect][2], readonly=True)

# choose how far you want to go back. Uncomment ALL (and comment SINCE) if you want to go through everything
# UIDs = conn.search(["ALL"])
UIDs = conn.search(["SINCE", datetime.date(2020, 1, 1)])

# collect links to open later
unsubscribeLinks = []

# search messages for "Unsubscribe" keyword and relevant link; update how many messages you want to search
for i in range(min(len(UIDs), 100)):
    rawMessage = conn.fetch([UIDs[i]], ["BODY[]", "FLAGS"])
    marker = UIDs[i]
    message = pyzmail.PyzMessage.factory(rawMessage[marker][b"BODY[]"])
    try:
        htmlObj = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(htmlObj, "html.parser")
        elems = soup.select("a")
        for e in range(len(elems)):
            if "Unsubscribe" in elems[e]:
                unsubscribeLinks.append(elems[e].get("href"))
                print("Success; link added.")
            else:
                print("No link found.")
    except:
        print("Operation failed. Moving to next message ...")

# pprint.pprint(unsubscribeLinks)
# open all unsubscribe links
for link in unsubscribeLinks:
    webbrowser.open(link)

# logout
conn.logout()