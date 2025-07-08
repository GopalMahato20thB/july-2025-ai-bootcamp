# Leetcode 01
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.
"""

def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
print(twoSum([1, 2, 5, 7], 12))        

