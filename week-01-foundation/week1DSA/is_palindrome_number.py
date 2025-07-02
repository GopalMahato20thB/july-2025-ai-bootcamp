"""
📝 Problem Statement: Palindrome Number
Given an integer x, return True if x is a palindrome, and False otherwise.
An integer is a palindrome when it reads the same backward as forward.
🔍 Examples:
python
Copy
Edit
Input: x = 121
Output: True
Input: x = -121
Output: False  # because -121 ≠ 121-
Input: x = 10
Output: False  # because 10 ≠ 01
🧾 Constraints:
You cannot convert the integer to a string (in some versions of the question).
Negative numbers are not palindromes.
You need to consider both digit reversal and symmetry.



"""
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_half = 0
    while x > reversed_half:
        digit = x % 10
        reversed_half = reversed_half * 10 + digit
        x = x // 10
    return x == reversed_half or x == reversed_half // 10

print(isPalindrome(123))

print(isPalindrome(121))
print(isPalindrome(-121))

    
        
