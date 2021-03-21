#! python3
# removeCsvHeader.py - Removes the first row (header) from all CSV in current working directory

import csv, os

os.makedirs("headerRemoved", exist_ok=True)

# Loop through every file in the cwd
for file in os.listdir("."):
    if not file.endswith(".csv"):
        continue                                # skip non-csv files

    print(f"Removing header from {file} ...")
    # Read the CSV file in (skipping first row)
    rows = []
    fileObj = open(file)
    readerObj = csv.reader(fileObj)
    for r in readerObj:
        if readerObj.line_num == 1:
            continue                            # skip first row
        rows.append(r)
    fileObj.close()

    # Write out the CSV file
    csvFileObj = open(os.path.join("headerRemoved", file), "w", newline="")
    csvWriter = csv.writer(csvFileObj)
    for r in rows:
        csvWriter.writerow(r)
    csvFileObj.close()