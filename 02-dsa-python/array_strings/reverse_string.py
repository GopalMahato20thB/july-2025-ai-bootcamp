"""
You’re given ["h", "e", "l", "l", "o"] and must reverse it in-place to ["o", "l", "l", "e", "h"].
"""

def reverse_(arr):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end - 1
    return arr
print(reverse_([1, 2, 3, 4, 5]))


