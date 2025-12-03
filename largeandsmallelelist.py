def largest_smallest_element(num):
    large_num = num[0]
    small_num = num[0]
    for i in num:
        if(i>large_num):
            large_num =i
        elif(i<small_num):
            small_num =i  

    print("the largest number is:", large_num)  
    print("the smallest number is:", small_num)  
      

num = [1,2,3,4,5,6,7,8,9]
print(largest_smallest_element(num))    