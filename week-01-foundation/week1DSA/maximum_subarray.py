"""
🧠 LeetCode 53 – Maximum Subarray
(A must-know question — famous for introducing Kadane’s Algorithm)
📜 Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum, and return its sum.
✏️ Example:
python
Copy code
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.
"""
def max_subarray(nums):
    max_sum = nums[0]
    sum_ = 0
    for n in nums:
        sum_ += n
        max_sum = max(max_sum, sum_)
        if sum_ < 0:
            sum_ = 0
        
    return max_sum

print(max_subarray([4, -1, 2, 1]))
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6

