"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

def length_of_last(s):  
    return len(s.split()[-1])

print(length_of_last("AI Engineer"))

"""
in place code
def length_of_last_word(s):
    length = 0
    i = len(s) - 1

    while i >= 0 and s[i] == ' ':
        i -= 1  # Skip trailing spaces

    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length

"""

