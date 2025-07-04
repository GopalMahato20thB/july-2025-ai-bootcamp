"""
🧠 LeetCode 58 – Length of Last Word
📜 Problem Statement:
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""
def lenght_last_word(string):
    list_form = string.split()
    return len(list_form[-1])
print(lenght_last_word("Gopal Mahato"))


