import csv

row_to_delete = 1 # Index of the row to delete

with open('delete.csv', mode='r', newline='') as file:
    rows = list(csv.reader(file))

if 0 <= row_to_delete < len(rows):
    del rows[row_to_delete]

with open('delete.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
