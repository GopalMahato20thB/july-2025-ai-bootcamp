"""
You are given a large integer represented as an array of digits, where each digit is an element in the list and the most significant digit is at the beginning.
Your task is to add one to this integer and return the resulting array of digits.
"""
def plus_one(arr):  
    for i in range(len(arr) - 1, - 1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        else:
            arr[i] = 0
    return [1] + arr

print(plus_one([9, 9, 9]))




