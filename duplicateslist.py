def duplicates(num):
    seen = set()
    duplicas = set()
    for i in num:
        if i in seen:
           duplicas.add(i)
        else:
            seen.add(i)     
    return list(duplicas)        

num = [0,1,2,3,2,1,3]  
print("the duplicates elements are:", duplicates(num))  

