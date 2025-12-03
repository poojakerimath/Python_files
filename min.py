def min_num(lst):
    min_num=lst[0]
    for i in lst:
        if(i<min_num):
            min_num=i
    return min_num

numbers=[1,2,3,4,4,5]
print("minimum_numbers:",min_num(numbers))      