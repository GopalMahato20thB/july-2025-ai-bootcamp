"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

After removing the duplicates, return the number of unique elements k.
You must do it in-place with O(1) extra memory.
"""

def remove_duplicates(arr):
    if not arr:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
            
    return i + 1
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))    
    
