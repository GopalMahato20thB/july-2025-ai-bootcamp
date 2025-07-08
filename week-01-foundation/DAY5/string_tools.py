"""
1. Create a module called string_tools.py with two functions:
    .reverse_string(s) - returns reverse string
    .is_palindrome(s) - returns True if the string is a palindrome

2. Create a main.py file to:
    >Import the module
    >Call both functions with user input    
"""
def reverse_integer(s):
    INT_MIN = 2**31
    INT_MAX = 2**31 - 1

    result = 0
    while s != 0:
        digit = s % 10
        s = s // 10

        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit % INT_MAX // 10):
            return 0
        
        result = result * 10 + digit
    return result 

# this program reverse integer

def reverse_string(s):
    return s[::-1]
def is_palindrome(s):
    s = s.lower()
    return s == reverse_string(s)
