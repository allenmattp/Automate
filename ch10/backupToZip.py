#! python3
# backupToZip.py - Copies an entire folder and its contents
# into a ZIP file whose filename increments.

import zipfile, os


def backupToZip(folder):
    # Back up the entire contents of parameter "folder" into a ZIP file

    folder = os.path.abspath(folder)    # arg for folder should be absolute path

    # Determine filename increment
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create the ZIP file.
    print(f"Creating {zipFilename} ...")
    backupZip = zipfile.ZipFile(zipFilename, "w")



    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername} ...")
        # Add current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all files in folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue    # skip backing up the backup files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("Task complete.")


if __name__ == '__main__':
    backupToZip("C:\\delicious")