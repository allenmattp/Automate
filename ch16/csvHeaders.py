import csv

exampleFile = open("exampleWithHeader.csv")
exampleDictReader = csv.DictReader(exampleFile)

for row in exampleDictReader:
    print(row["Timestamp"], row["Fruit"], row["Quantity"])

example2File = open("example.csv")
example2DictReader = csv.DictReader(example2File, ["Time", "Name", "Amount"])

examp
for row in example2DictReader:
    print(row)