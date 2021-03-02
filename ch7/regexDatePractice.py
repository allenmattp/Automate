"""
Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12,
and the years range from 1000 to 2999.
Note that if the day or month is a single digit, it’ll have a leading zero.

From text copied on clipboard, finds all patterns that match the DD/MM/YYYY format.
prints date if it is valid, otherwise prints "Not valid: date"
"""
import pyperclip, re

text = str(pyperclip.paste())

dateRegex = re.compile(r"(\d\d)/(\d\d)/(\d\d\d\d)")

dates_found = dateRegex.findall(text)
dates = []

# validate date
for d in dates_found:
    valid = False
    leap = False
    day, month, year = d
    if not int(year) % 4 and (int(year) % 100 or not int(year) % 400):   # determine if leap year
        leap = True
    if int(month) == 2 and leap:    # if Feb and leap year
        if int(day) <= 29:
            valid = True
    elif int(month) == 2 and not leap:      # if Feb and not leap year
        if int(day) <= 28:
            valid = True
    if int(month) in [4, 6, 9, 11] and int(day) <= 30:      # if a 30 day month
        valid = True
    if int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) <= 31:    # if a 31 day month
        valid = True
    if valid:
        date = (day + "/" + month + "/" + year)
    if not valid:
        date = ("Not valid: " + day + "/" + month + "/" + year)
    dates.append(date)


for d in dates:
    print(d)