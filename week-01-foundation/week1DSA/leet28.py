"""
✅ Problem 2: LeetCode 28 – Implement strStr()
📘 Problem:
Return the index of the first occurrence of a substring (needle) in a string (haystack). Return -1 if not found.
Example:
Copy code
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
"""
def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):  # Slide a window of size m
        if haystack[i:i+m] == needle:
            return i
    return -1

        
