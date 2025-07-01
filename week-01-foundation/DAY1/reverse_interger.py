"""
🔁 Problem: Reverse Integer
Given a signed 32-bit integer x, reverse its digits.
Return the reversed integer.
If reversing x causes the value to go outside the 32-bit signed integer range [-2³¹, 2³¹ - 1], then return 0.
🧾 Constraints:
-2³¹ <= x <= 2³¹ - 1 → i.e., -2147483648 to 2147483647
You cannot store the result as a 64-bit integer or use built-in overflow-safe data types in some languages.
Input: x = 123
Output: 321
Input: x = -123
Output: -321
Input: x = 120
Output: 21
Input: x = 1534236469
Output: 0  # Reversed integer overflows
"""
"""

def reverse_num(num):
    # defining 32-bit limits
    INT_MIN = -2**31 
    INT_MAX = 2**31 - 1
    # handling the sign
    sign = -1 if num < 0 else 1
    num = abs(num) #working with positive number
    
    result = 0
    while num != 0:        
        #extracting the last digit
        digit = num %  10        
        #removing the last digit
        num = num // 10
        if result > INT_MAX // 10:
            return 0
        if result == INT_MAX // 10 and digit > INT_MAX % 10:
            return 0
        result = result * 10 + digit
        
    return sign * result    
    
test_cases = [
        123,           # Expected: 321
        -123,          # Expected: -321
        120,           # Expected: 21
        0,             # Expected: 0
        1534236469,    # Expected: 0 (overflow)
        -2147483648,   # Expected: 0 (overflow)
        1463847412,    # Expected: 2147483641
        -1463847412,   # Expected: -2147483641
    ]
    

for num in test_cases:
    result = reverse_num(num)
    print(f"Input: {num:>12} → Output: {result}")
"""

##practice another time 
def reverse_integer(x):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1 
    
    sign = - 1 if x < 0 else 1
    x = abs(x)
    
    result = 0
    
    while x != 0:
        digit = x % 10
        x = x // 10
        
        if result > INT_MAX // 10:
            return 0
        if result == INT_MAX // 10 and digit % INT_MAX // 10:
            return 0
        result = result * 10 + digit
    return sign * result
    
    
print(reverse_integer(123))    


