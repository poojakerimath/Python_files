def LCM(num1,num2):
    original_num1 ,original_num2= num1,num2
    while(num2!=0):
        num1,num2 = num2,num1%num2

#compute the lcm with formula
    lcm = (original_num1*original_num2)//num1
    return lcm

num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
print("the Given LCM of the number is:", LCM(num1,num2))