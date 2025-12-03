'''
#manually using for loop here
n = input("enter the word: ")
count = 0
for i in n:
    count+=1
print("The total number is:", count)
'''

#using built-in functions len
n = input("enter the word: ")
word = len(n)
print("The total length of the given word is:", +word)