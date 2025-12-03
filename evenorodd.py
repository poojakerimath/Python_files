def even_or_odd(num):
    even_list = []
    odd_list =[]
    for i in num:
        if(i%2==0):
            even_list.append(i)
        else:
            odd_list.append(i)    
    print ("The even list integers are:", even_list)
    print("The odd list integers are:", odd_list)
            
num = [1,2,3,5,8,9,10,23,34]
(even_or_odd(num))
