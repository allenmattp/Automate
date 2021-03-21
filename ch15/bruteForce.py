#! python3
# open an encrypted pdf using brute force
# only works if password is a single english word (found in provided dictionary)

import PyPDF2
from time import time

filePath = "encryptedfile.pdf"                                  # PDF to crack
start = time()                                                  # Track runtime
success = False                                                 # Track if password has been found


def decryptTry(filename, password):
    try:
        pdfReader = PyPDF2.PdfFileReader(open(filename, "rb"))  # PyPDF2 needs to reload pdf each attempt
        pdfReader.decrypt(password)                             # enter a password
        pdfReader.getPage(0).extractText()                      # try to read page, will throw error if still encrypted
        print(f"Success! Password is {guess}.")
        print(f"Time to crack: {time() - start} seconds.")
        return True
    except:
        return False


print("Hacking in progress ...")
with open("dictionary.txt", "r") as f:                          # list of words, one per line
    line = f.readline().strip()
    while line and not success:                                 # go through each line in dictionary
        guess = line.lower()                                    # try word with lower case
        success = decryptTry(filePath, guess)
        if not success:
            guess = line.upper()                                # try word with upper case
            success = decryptTry(filePath, guess)
        line = f.readline().strip()                             # prepare next word

    if not success:
        print("This password cannot be cracked.")               # no guesses were successful
        print(f"Tried for: {time() - start} seconds.")

f.close()