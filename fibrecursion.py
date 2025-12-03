def fibbonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)

n = int(input("enter the value you want to enter: ")  ) 
print(fibbonacci(n))