def count_occurences(num):
    duplicates = {}
    for i in num:
        if i in duplicates:
            duplicates[i]+=1
        else:
            duplicates[i] =1
    
    print("the count occurences in list:", duplicates)
num = [1,2,3,4,5,5,6,7]
count_occurences(num)