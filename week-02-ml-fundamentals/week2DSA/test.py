# Before solving Day 7 of week2 DSA problems if i need to know some concept related problems Then i will master them
#Problem1 leetcode 27 - remove element Concepts i need to know 1. array traversal 2. Two-pointer technique(when modifying array in-place)
# 3 In-place update vs return new array
#mini task 1.1: basic array traversal Tasks is try changing value 3 to -1
"""
nums = [3, 2, 2, 3]
for i in range(len(nums)):
    if nums[i] == 3:
        nums[i] = -1
print(nums) 
"""

"""
## mini task 1.2: Two-pointer In-Place Filter
nums = [1, 2, 2, 3, 4]
target = 2 
# write a code to remove all 2s and shift the rest to the left,  don't use extra array
"""

#frist i need a variable that will keep print numbers which are not 2s
#i will increment that variable after assigning not 2s value
"""
nums_copy = nums.copy()

i = 0
for j in range(len(nums)):
    print(nums[j])
    if nums[j] != 2:
        nums[i] = nums[j]
        i += 1

print("Original array: ", nums_copy)
print("After removing 2s: ", nums)
"""


"""
Problem2: leetcode 34- Find First and Last Position
Concept needed:
1. Binary search
2. Handling duplicates in sorted array
3. Left and right boundary logic
"""
## mini Task 2.1: Classic Binary search
arr = [1, 3, 5, 7, 9]
target = 5
# write binary search and return the index of the target

def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1


print(binary_search(arr, target)) 
print(binary_search([1, 2, 3], 3)) 





            