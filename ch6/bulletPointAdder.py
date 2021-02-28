#! python3

import pyperclip

text = pyperclip.paste() # take in text in clipboard

# TODO: manipulate clipboard text in some way
print(text)

pyperclip.copy(text) # return text to clipboard