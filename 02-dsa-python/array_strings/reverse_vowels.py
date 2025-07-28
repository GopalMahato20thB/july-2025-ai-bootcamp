"""
📌 Problem Statement Summary:
Given a string s, reverse only the vowels of the string and return it.
Practice Example:
Input:  "hello"
Output: "holle"

Input:  "leetcode"
Output: "leotcede"

Input: s = "IceCreAm"
Output: "AceCreIm"

"""
def reverse_vowels(s):
    s = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] not in vowels:
            start += 1
        elif s[end] not in vowels:
            end -= 1
        else:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
    return "".join(s)        
            
print(reverse_vowels("hello"))
print(reverse_vowels("leetcode"))
print(reverse_vowels("IceCreAm"))






