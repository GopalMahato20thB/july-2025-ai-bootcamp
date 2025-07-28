"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

You must do this in-place (i.e., without making a new array), and try to minimize the total number of operations.

Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
"""
def move_zeros(nums):   
    insert_pos = 0
    
    for num in nums:    
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
        
    return nums    
print(move_zeros([0, 1, 0, 3, 12]))        
