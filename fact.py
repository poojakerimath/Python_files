def factorial(num):
    if num <0:
        return "sorry factorial numbers can't be in negative"
    elif(num==0 or num==1):
        return 1
    else:
        result= 1
        for i in range(2,num+1):
            result*=i
    return result

num = 5
print(f"Factorial of {num} is a {factorial(num)}")

       
   
        
    
    
    
    







