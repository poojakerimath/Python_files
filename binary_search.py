def binary_search(arr,target):
    left, right = 0,len(arr)-1
    
    while(left<=right):
        mid = (left+right)//2
        if(arr[mid]==target):  
           return mid
        elif(arr[mid]<target):    
            left = mid+1
        else:
            right = mid-1
        
        '''
        #used when given array is in descending order
        if(arr[mid]>target):    
            left = mid+1
        else:
            right = mid-1
        '''    

    return -1

arr = [9,8,7,6,5,4,3,2,1]
target = 9
result =binary_search(arr,target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
