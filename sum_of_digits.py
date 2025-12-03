def sum_of_digits(n):
    total =0
    while n>0:
        digits = n%10
        total = total+digits
        n//=10
    return total    


n = int(input("enter the number"))
print("The total sum of the digits:",sum_of_digits(n))