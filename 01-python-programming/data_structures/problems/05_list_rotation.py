## Rotate a list by k positions.

def reverse_list(l, start, end):
    while start <= end:
        l[start], l[end] = l[end], l[start]
        start, end = start + 1, end - 1
    return l

def rotate_k_position(nums, k):
    n = len(nums)
    k = k % n
    start = 0
    end = n - 1
    reverse_list(nums, start, end)
    reverse_list(nums, start, k - 1)
    reverse_list(nums, k, end)
    return nums
    
print(rotate_k_position([1, 2, 3, 4, 5], 2))    
    

