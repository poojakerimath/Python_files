import csv
with open('second.csv', mode= 'w',newline='') as file:
     writer=csv.writer(file)
     writer.writerow(['Name','Age','Department'])
     writer.writerow(['Alice','22','cs'])
     writer.writerow(['Bob','23','ec'])
     writer.writerow(['charlie','25','e&e'])
     writer.writerow(['Alice','26','mech'])
     writer.writerow(['lakshmi','24','civil'])
     writer.writerow(['ravi','31','ec'])

print("CSV file created successfully.")

    
    
