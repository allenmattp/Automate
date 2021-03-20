import PyPDF2


pdfReader = PyPDF2.PdfFileReader(open("encrypted.pdf", "rb"))

if pdfReader.isEncrypted:
    print("This pdf is encrypted.")
    password = input("Enter the password: ")
    pdfReader.decrypt(password)
else:
    print("This pdf is not encrypted.")

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())