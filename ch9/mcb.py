#! python3
"""
mcb.py - Saves and loads pieces of text for clipboard use
          updated version to accept user input while cmd running,
          rather than requiring args passed upon initialization
 Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
        py.exe mcb.pyw del <keyword> - Removes a saved keyword
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
        py.exe mcb.pyw list - Loads all keywords to clipboard
        py.exe mcb.pyw delall - Clears all saved keywords
        """

import sys, pyperclip, shelve, pprint

def main():

    mcbShelf = shelve.open("mcb")
    while True:

        key_list = pprint.pformat(list(mcbShelf.keys()))
        print("Current keywords:")
        print(key_list, "\n")

        entry = str(input(
    """
Please make your selection:\n
save <keyword> - saves clipboard to keyword
del <keyword> - removes a saved keyword
<keyword> - loads keyword's clipboard
list - copy all keywords to clipboard
delall - clears all saved keywords
quit - close program\n\n
    """)).split()
        entry = [e.lower() for e in entry]

        if len(entry) == 2:
            if entry[0] == "save":
                mcbShelf[entry[1]] = pyperclip.paste()
                print(f"Clipboard saved as {entry[1]}.\n\n")
            elif entry[0] == "del":
                del mcbShelf[entry[1]]
                print(f"Keyword {entry[1]} removed.\n\n")
            else:
                print("Invalid selection. Please try again!\n\n")

        elif len(entry) == 1:
            if entry[0] == "list":
                pyperclip.copy(pprint.pformat(list(mcbShelf.keys())))
                print("Keywords copied to clipboard.\n\n")
            elif entry[0] == "delall":
                mcbShelf.clear()
                print("Keywords cleared.\n\n")
            elif entry[0] in mcbShelf:
                pyperclip.copy(mcbShelf[entry[0]])
                print("Copied to clipboard!\n\n")
            elif entry[0][0] == "q":
                mcbShelf.close()
                sys.exit()
            else:
                print("Invalid selection. Please try again!\n\n")

        else:
            print("Invalid selection. Please try again!\n\n")


if __name__ == '__main__':
    print("Welcome!\n\n")
    main()