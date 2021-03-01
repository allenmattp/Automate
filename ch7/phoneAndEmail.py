#! python3
# phoneAndEmail.py: Finds phone numbers and email addresses from clipboard

import pyperclip
import re


phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                          # area code
    (\s|-|\.)?                                  # separator
    (\d{3})                                     # first 3 digits
    (\s|-|\.)                                   # separator
    (\d{4})                                     # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?              # extension
    )""", re.VERBOSE)


emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+                           # username
    @                                           # '@'
    [a-zA-Z0-9.-]+                              # domain
    (\.[a-zA-Z]{2,4})                           # dot-something
    )""", re.VERBOSE)


text = str(pyperclip.paste())                   # grab clipboard text and convert to string

matches = []                                    # collect matches in a list
for g in phoneRegex.findall(text):              # find and format phone:
    phoneNum = "-".join([g[3], g[5]])           # 888-555-2020 x123
    if g[1]:                                    # if there's an area code...
        phoneNum = g[1] + "-" + phoneNum
    if g[8]:                                    # if there's an extension...
        phoneNum += " x" + g[8]
    matches.append(phoneNum)
for g in emailRegex.findall(text):              # leave email as-is
    matches.append(g[0])

if len(matches):                                # return results, if any
    pyperclip.copy("\n".join(matches))
    print("Results found: copied to clipboard\n\n\n")
    print("\n".join(matches))
else:
    print("No results found.")