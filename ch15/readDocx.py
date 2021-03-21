#! python3

import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for p in doc.paragraphs:
        fullText.append("  " + p.text)
    return "\n".join(fullText)

print(getText("demo.docx"))