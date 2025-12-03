def factorial(n):
    if n <0:
        print( "negative numbers are invalid")
    elif n==0 or n==1:
        return 1
    fact=1
    for i in range(2, n+1):
        fact*=1
    return  fact

n = int(input("enter the value you want to enter "))    
print(factorial(n))