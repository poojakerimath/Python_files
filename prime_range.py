def prime_numbers(start,end):
    prime=[]
    for i in range(start,end+1):
        if(i<=1):
            continue
        is_prime = True
        for j in range(2, int(i*0.5)+1):
            if(i%j==0):
                is_prime = False
                break
        if(is_prime):
            prime.append(i)
    return prime            

start = int(input("enter the number you want to start the prime"))
end = int(input("enter the number you want to end the prime"))
print(prime_numbers(start,end))