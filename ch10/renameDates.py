#! python3
# renameDates.py - Renames filenames w/American MM-DD-YYYY format
# to European DD-MM-YYYY

import shutil, os, re


# Create a regex that matches files with the American date format.
datePattern = re.compile("""
^(.*?)                          # all text before the date
(([01])?\d)-                     # one or two digits for the month
(([0123])?\d)-                 # one or two digits for the day
((19|20)\d\d)                   # four digits for the year
(.*?)$                          # all text after the date
""", re.VERBOSE)

# Loop over the files in the working directory.
for ameriFilename in os.listdir("."):
    mo = datePattern.search(ameriFilename)

# Skip files without a date.
    if mo is None:
        continue

# Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# Form the European-style filename.
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

# Get the full, absolute paths.
    absWorkingDir = os.path.abspath(".")
    ameriFilename = os.path.join(absWorkingDir, ameriFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

# Rename the files.
    print(f"Renaming '{ameriFilename}' to '{euroFilename}' ...")
    # shutil.move(ameriFilename, euroFilename) # Uncomment AFTER testing