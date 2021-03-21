#! python3
# combinePDFv2.py - Combines all the PDFs in current working directory into a single PDF

import PyPDF2, os


pdfFiles = []
# add all PDFs in current directory to list
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files
for pdf in pdfFiles:
    pdfFileObj = open(pdf, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# Loop through all the pages (except for the cover) and add them to file
    if pdfReader.isEncrypted:
        print(f"{pdf} is encrypted, skipping ...")
    else:
        print(f"Adding {pdf} ...")
        for pageNum in range(1, pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))

# Save the resulting PDF to a file
resultPdf = open("combinedPDF.pdf", "wb")
pdfWriter.write(resultPdf)
resultPdf.close()

print("Done.")



