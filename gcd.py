def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a
print(gcd(48,18))   # manually calculated with gcd




import math
a = 8
b = 12
print(math.gcd(a, b))  #using math as in-bulit function

