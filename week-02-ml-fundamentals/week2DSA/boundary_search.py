## Given an sorted array and a target, return the first and the last index of that target.

def left_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid 
            right = mid - 1 # keep going left
        elif arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

    return result 


def right_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid 
            left = mid + 1 # keep going right
        elif arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

    return result 

# combining both
def search_range(arr, target):
    return [left_bound(arr, target), right_bound(arr, target)]

print(search_range([1, 2, 2, 2, 3, 4], 2))                                