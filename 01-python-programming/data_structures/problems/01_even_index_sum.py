## Given a list of numbers, return the sum of elements at even indexes.

def sum_evens_indces(nums):  
    sum_of_evens_indexs = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            sum_of_evens_indexs += i
    return sum_of_evens_indexs

print(sum_evens_indces([1, 2, 3, 4, 5, 6]))    
            
        

