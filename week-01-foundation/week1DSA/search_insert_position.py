"""
✅ Problem 3: LeetCode 35 – Search Insert Position
📘 Problem:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be inserted in order.
Example:
Input: nums = [1,3,5,6], target = 5
Output: 2
"""
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        
    return left
print(search_insert([1, 3, 4, 7, 10], 6))


