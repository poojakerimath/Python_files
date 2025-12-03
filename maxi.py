def max_num(list):
    max_num=list[0]
    for i in list:
       if(i>max_num):
        max=i
    return max  

list = [12,11,13,14,19]
print(max_num(list))

        