import csv

outputFile = open("output.csv", "w", newline="")
outputWriter = csv.writer(outputFile)

outputWriter.writerow([x for x in range(0, 10)])
outputWriter.writerow([x for x in range(0, 20, 2)])
outputWriter.writerow([x for x in range(0, 30, 2)])

outputFile.close()

readFile = open("output.csv")
fileReader = csv.reader(readFile)
for row in fileReader:
    print(str(row))

