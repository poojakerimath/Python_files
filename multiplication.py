'''
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list =[]
for i in my_list:
    if i in my_list:
        mul=i*2
    new_list.append(mul)
print("the multiplication table is:",new_list)        
'''

multiplication_table = int(input("enter the number you want to enter: "))
empty_list = []

for i in range(1,10):
    product = i*multiplication_table
    row = (str)(multiplication_table)+ "*" +str( i) + "=" + str(product)
    empty_list.append(row)

print("The multiplication table:", multiplication_table )    
for row in empty_list:
    print(row)

