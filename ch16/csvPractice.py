import csv


exampleFile = open("example.csv")
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print(f"{str(exampleReader.line_num)} {str(row)}")

# read object can be looped over only once
example2File = open("example.csv")
example2Reader = csv.reader(example2File)
exampleData = list(example2Reader)

for d in exampleData:
    print(d)