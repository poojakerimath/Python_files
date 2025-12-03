
def reverse_number(num):
    rev =0
    while num>0:
      digits=num%10
      rev = rev*10+digits
      num//=10
    return rev 

    

num=12345
print(reverse_number(num))#using the function code 


''''''
num = 1234
rev=0
while num>0:
   digits=num%10
   rev=rev*10+digits
   num//=10
print("Reversed number:" ,rev)
''''''