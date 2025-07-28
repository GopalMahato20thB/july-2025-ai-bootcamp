"""
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def two_sum(nums, target):
    """
    Returns indices of the two numbers such that they add up to target.
    """
    track = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in track:
            return [track[diff], i]
        track[n] = i    
    

# Example Test
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Input:", nums, "Target:", target)
    result = two_sum(nums, target)
    print("Output:", result)

