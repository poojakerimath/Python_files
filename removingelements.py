my_list = [0,1,2,3,4,5,6]
my_list.remove(0) #remove by value
my_list.pop() #remove the last element
my_list.pop(1) #remove the element at index 1
print(my_list)

#Slicing means taking a subset of elements from a sequence using the syntax:
#sequence[start:stop:step]
#start → Index where the slice begins (inclusive).
#stop → Index where the slice ends (exclusive).
#step → How much to increment (or decrement) each time

nums = [0,1,2,3,4,5]
print(nums[1:4]) #removes element index 1 to 3

print(nums[:3]) #[0,1,2] start from beginning
print(nums[3:]) #[3,4,5] till end
print(nums[-3:]) #[3,4,5] last three elements,negative indices

#slicing strings
text = 'python'
print(text[0:4])
