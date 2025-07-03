"""
✅ Problem 1: LeetCode 26 – Remove Duplicates from Sorted Array
📘 Problem:
Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length.
Example:
Input: nums = [1,1,2]
Output: 2, nums becomes [1,2,_]
🎯 Goal: Remove duplicates in-place and return the new length.
"""

def remove_duplicates(nums):
    if not nums:
        return 0 
    i = 0
    for j in range(1, (len(nums))):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
print(remove_duplicates([1, 2, 2, 2, 3, 3, 3, 4, 7]))

        
