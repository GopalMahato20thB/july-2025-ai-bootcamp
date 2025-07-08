
"""
Given an integer array nums and an integer value val, remove all occurrence of val
in-place and return the new length of the array.
"""
def remove_element(arr, val):
    i = 0
    for j in range(len(arr)):
        if arr[j] != val:
            arr[i] = arr[j]
            i += 1
    return i 

print(remove_element([3, 2, 2, 3], 3))
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))

