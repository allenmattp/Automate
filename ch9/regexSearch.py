#! python3

# regexSearch.py - With user-supplied RegEx,
# searches all .txt files in the specified directory
# Returns filename and line number for any matches

from pathlib import Path
import re


activePath = input("Enter absolute directory path or leave blank for cwd:\n")
if activePath:
    activePath = Path(activePath)
else:
    activePath = Path.cwd()

print(f"Searching {activePath}\n\n")

searchTerm = re.compile(input("Enter search term:\n"))



for textFile in list(activePath.glob("*.txt")):
    print(f"\nSearching {textFile} ... \n")
    with open(textFile, "r") as file:
        lines = file.read().splitlines()
        for count, line in enumerate(lines):
            search = searchTerm.findall(line)
            if search:
                print(f"{search} found in {Path(textFile).name}, line {count + 1}.")
    file.close()