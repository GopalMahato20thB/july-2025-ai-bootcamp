"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum, and return its sum.


Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""
def max_subarray(arr):
    current_sum = 0
    max_sum = arr[0]
    
    
    for i in arr:
        current_sum += i
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum         

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))    
