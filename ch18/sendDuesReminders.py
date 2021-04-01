#! python3
# sendDuesReminders.py - Sends emails based on payment status in spreadsheet

import openpyxl, smtplib, sys


# Open spreadsheet and check dues status
wb = openpyxl.load_workbook("duesRecords.xlsx")
ws = wb.get_sheet_by_name("Sheet1")
lastCol = ws.max_column
latestMonth = ws.cell(row=1, column=lastCol).value

# TODO: Check each member's payment status


# TODO: Log into email account


# TODO: Send out reminder emails