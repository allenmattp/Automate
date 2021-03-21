#! python3
# Add encryption to a PDF doc

import PyPDF2


password = input("Select a password: ")
pdfFile = open("meetingminutes.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt(password)

resultPdf = open("encryptedfile.pdf", "wb")
pdfWriter.write(resultPdf)
resultPdf.close()

print("Done.")