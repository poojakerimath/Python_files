def reverse(num):
    rev = num[::-1]
    print(rev)
num = [0,1,2,3,4,5,6]    
print("The reversed list:", reverse(num))

def rev_num(n):
    rev = []
    for i in range(len(n) -1, -1,-1):
        rev.append(n[i])
    return rev   

n = [0,1,2,3,4,5]   
print("The reverse list:", rev_num(n)) 