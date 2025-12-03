import csv
with open('first.csv',mode = 'r') as file:
    reader=csv.reader(file)
    for read in reader:
        print(read)

        