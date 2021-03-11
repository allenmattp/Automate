#! python3
# fileSizeSearch.py - walks through given folder and all subfolders
# returning abs path of all files that meet minimum size threshold

import os

def fileSize(folder, bytes):

    for folderName, subfolders, filenames in os.walk(folder):

        for filename in filenames:
            absWorkingDir = os.path.join(folderName, filename)
            if os.path.getsize(absWorkingDir) > bytes:
                print(f"File in {folderName}:\n{filename}")
                print(f"{round(os.path.getsize(absWorkingDir) / 1000000, 2)} MB")

    print("")

if __name__ == '__main__':
    folder = input("Enter absolute file path:\n")
    bytes = int(input("Enter minimum byte size (leave blank for 10MB):\n",) or "10000000")
    fileSize(folder, bytes)