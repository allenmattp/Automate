#! python3
# backupToZip.py - Copies an entire folder and its contents
# into a ZIP file whose filename increments.

import zipfile, os


def backupToZip(folder):
    # Back up the entire contents of arg "folder" into a ZIP file

    folder = os.path.abspath(folder)    # folder path should be absolute

    # Determine filename increment
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number += 1

    # TODO: Create the ZIP file.


    # TODO: Walk the entire folder tree and compress the files in each folder
    print("Task complete.")


if __name__ == '__main__':
    backupToZip("C:\\delicious")