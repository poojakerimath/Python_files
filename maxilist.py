def max_element(num):
    max_val = num[0]
    for i in num:
        if i>= max_val:
            max_val = i
    return max_val        
num = [0,1,2,3,4,5,6]
print("The maximum element:",max_element(num))


def min_element(num):
    min_val = num[0]
    for i in num:
        if i<=min_val:
            min_val = i
    return min_val    
num = [1,2,3,4,5,6]
print("The minimum element:",min_element(num))   