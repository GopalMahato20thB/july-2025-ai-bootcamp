"""
Problem:
You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, and an integer target.
Return the indices of the two numbers such that they add up to target.
The answer must be returned as an array [index1, index2] of the two numbers, and index1 < index2.

You may not use the same element twice.

You must solve it using only constant extra space
"""
def two_sum2(arr,  target):
    start, end = 0, len(arr) - 1
    
    while start < end:
        current_sum = arr[start] + arr[end]
        
        if current_sum > target:
            end -= 1
        elif current_sum < target:
            start += 1
        else:
            return [start + 1, end + 1]
numbers, target = [2,7,11,15],  9
print(two_sum2(numbers, target))
