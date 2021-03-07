#! python3
# mcb.py - Saves and loads pieces of text for clipboard use
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw del <keyword> - Removes a saved keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard
#        py.exe mcb.pyw delall - Clears all saved keywords

import sys, pyperclip, shelve

def main():
    mcbShelf = shelve.open("mcb")

    if len(sys.argv) == 3:
        if sys.argv[1].lower() == "save":
            mcbShelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == "del":
            del mcbShelf[sys.argv[2]]
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == "list":
            pyperclip.copy(str(list(mcbShelf.keys())))
            print(pyperclip.paste())
        elif sys.argv[1].lower() == "delall":
            mcbShelf.clear()
        elif sys.argv[1].lower() in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print("""
    Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
           py.exe mcb.pyw del <keyword> - Removes a saved keyword
           py.exe mcb.pyw <keyword> - Loads keyword to clipboard
           py.exe mcb.pyw list - Loads all keywords to clipboard
           py.exe mcb.pyw delall - Clears all saved keywords
        """)

    mcbShelf.close()

if __name__ == '__main__':
    main()