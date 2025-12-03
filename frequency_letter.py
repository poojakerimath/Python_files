def count_the_frequency(s):
    count ={}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] =1 
    return count              


s = "hello world"
print(count_the_frequency(s))