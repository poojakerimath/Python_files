def count_the_digits(n):
    count =0
    while n>0:
        count+=1
        n//=10
    return count    
    print("The total number:", +count)  
n=int(input("enter the number given by the user"))
print(count_the_digits(n))
 