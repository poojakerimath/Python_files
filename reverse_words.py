def reverse_words(n):
    rev = ""
    for i in n:
        rev = i+rev
    print("The reverse word:", rev)    
   
n= input("enter the words you want to enter")  
print(reverse_words(n))      
            
