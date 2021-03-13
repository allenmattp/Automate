#! python3
# mapIt.py - launches google maps in browser
# using address from command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)