#! python3
# save txt file to spreadsheet where each line = a row

import openpyxl

txtFile = input("enter txt filename (with extension):")
xlsxFile = input("enter excel filename (no extension):")
seperator = input("enter desired separator:") or " "

wb = openpyxl.Workbook()
ws = wb.active

print("Reading text file ...")
with open(txtFile, "r") as txt:
    line = txt.readline()
    row_count = 1
    while line:
        splitLine = line.split(seperator)   # specify separator appropriate for your text file
        col_count = 1
        for split in splitLine:             # write to worksheet
            ws.cell(row=row_count, column=col_count).value = split
            col_count += 1
        line = txt.readline()
        row_count += 1

wb.save(xlsxFile + ".xlsx")

print("Done.")