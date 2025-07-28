"""
Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

An input string is valid if:
>>> Open brackets are closed by the same type of brackets.
>>> Open brackets are closed in the correct order.
>>> Every closing bracket has a corresponding open bracket of the same type.
"""

def invalid(s):
    hashmap = { ")": "(", "]": "[", "}": "{" }
    
    stk = []
    
    for char in s:
        if char not in hashmap:
            stk.append(char)
        else:
            if not stk or stk.pop() != hashmap[char]:
                return False
    return not stk                        
    
print(invalid("()"))
print(invalid("([]){}"))

