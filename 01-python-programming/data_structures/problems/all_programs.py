## Given a list of numbers, return the sum of elements at even indexes.

def sum_evens_indces(nums):  
    sum_of_evens_indexs = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            sum_of_evens_indexs += i
    return sum_of_evens_indexs

print(sum_evens_indces([1, 2, 3, 4, 5, 6]))    

### Return the difference between max and min element in list.

def diff_max_min(l):
    return max(l) - min(l)

print(diff_max_min([1, 2, 3, 4, 5,  6, 7]))                
        
### Remove all duplicates from a list.

def remove_duplicates_list(l):
    unique_l = []
    for i in l:
        if i not in unique_l:
            unique_l.append(i)
    return unique_l

print(remove_duplicates_list([1, 3, 4, 5, 7, 7, 7, 9, 9]))

 ## Find common elements between two lists.
 
def common_elements(l1, l2):
    return list(set(l1) & set(l2))       

print(common_elements([1, 3, 5, 6, 9, 7], [7]))

## Rotate a list by k positions.

def reverse_list(l, start, end):
    while start <= end:
        l[start], l[end] = l[end], l[start]
        start, end = start + 1, end - 1


def rotate_k_position(nums, k):
    n = len(nums)
    k %= n
    reverse_list(nums, 0, n - 1)
    reverse_list(nums, 0, k - 1)
    reverse_list(nums, k, n - 1)
    return nums
    
print(rotate_k_position([1, 2, 3, 4, 5], 2))    
    
## Find the second largest number in a list.

def second_largest(l):  
    max_value = float("-inf")
    second_max = float("-inf")
    for i in l:
        if i > max_value:
            second_max = max_value
            max_value = i
        elif max_value > second_max > i:
            second_max = i
    return second_max if second_max != float("-inf") else None        
            
print(second_largest([1, 3, 4, 7]))        

### Reverse a list without using reverse() or slicing.
def reverse_list(l):
    start, end = 0, len(l) - 1
    while start <= end:
        l[start], l[end] = l[end], l[start]
        start, end = start + 1, end - 1
    return l

print(reverse_list([1, 2, 4, 6, 7]))  


 ### From a list, return a new list of even numbers.
 
def filter_evens(l):
    return [i for i in l if i % 2 == 0]
print(filter_evens([1, 2, 4, 6, 7]))    

## Given list of strings, return list of their lengths.

## Given list of strings, return list of their lengths.

def lengths_of_each(l):
    return [ len(s) for s in l ]


print(lengths_of_each(["hello", "world", "python", "code"])) 
 #Merge two lists and return a sorted list without duplicates.
 
def merge_and_sort(l1, l2):    
    return sorted(set(l1 + l2))
print(merge_and_sort([1, 3, 5, 7],[2, 3, 6, 7, 8])) 

