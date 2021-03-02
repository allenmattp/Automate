"""
A strong password is defined as one that is at least eight characters long,
contains both uppercase and lowercase characters,
and has at least one digit.
"""

import pyperclip, re

text = str(pyperclip.paste())

upper_re = re.compile(r"[A-Z]")
lower_re = re.compile(r"[a-z]")
digit_re = re.compile(r"[0-9]")

upper = upper_re.findall(text)
lower = lower_re.findall(text)
digit = digit_re.findall(text)

if upper and lower and digit and len(text) >= 8:
    print("Strong password!")
else:
    print("Weak password.")