"""
Given a string s, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
"""
def first_uniq_char(s):
    count = {}
    
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
print(first_uniq_char("leetcode"))       
print(first_uniq_char("loveleetcode"))   
print(first_uniq_char("aabb"))    
        
