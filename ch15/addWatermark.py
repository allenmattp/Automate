#! python3
# overlay a watermark/image over first page of a pdf
# creates a new file

import PyPDF2

# file to add watermark to
mainFile = open("meetingminutes.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(mainFile)
firstPage = pdfReader.getPage(0)

# file with watermark
pdfWatermarkReader = PyPDF2.PdfFileReader(open("watermark.pdf", "rb"))

# add watermark
firstPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(firstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open("watermarkedCover.pdf", "wb")
pdfWriter.write(resultPdfFile)
mainFile.close()
resultPdfFile.close()

print("Done.")