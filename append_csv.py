import csv
with open ('write.csv', mode='a', newline='') as file:
    write=csv.writer(file)

    write.writerow(['rekha','43','ai'])
    