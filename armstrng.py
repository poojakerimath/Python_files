def arm_strong(num):
    original_num=num
    num_of_digits = len(str(num))
    armstrong_num=0
    while num>0:
        digits = num%10
        armstrong_num+=digits**num_of_digits ##helps to raise the digits by itself.
        num//=10
    return armstrong_num == original_num

num = int(input("enter the number given by the user"))
print("Armstrong_number:", arm_strong(num))
