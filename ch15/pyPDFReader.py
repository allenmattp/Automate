import PyPDF2

pdfFileObj = open("meetingminutes.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page)
    print(pageObj.extractText())

pdfFileObj.close()