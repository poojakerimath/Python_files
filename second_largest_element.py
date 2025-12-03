nums = [1,2,3,4,5,6]
sec_max = float('-inf')
max_val = float('-inf')
for num in nums:
    if(num>max_val):
        sec_max = max_val
        max_val = num
    elif(num>sec_max and num!=max_val):
        sec_max = num
print("The second largest element is:", +sec_max)
