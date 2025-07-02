"""
🔢 Day 2 DSA Challenge 1: Roman to Integer (LeetCode 13)
📝 Problem Statement:
Given a Roman numeral string s, convert it to an integer.
Symbol       Value
I               1
V               5
X              10
L              50
C             100
D             500
M            1000
"""
def roman_to_int(s):
    roman_map = {
            "I": 1, 
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    sum_ = 0

    for i in range(len(s) - 1):
        if roman_map[s[i]] < roman_map[s[i + 1]]:
            sum_ -= roman_map[s[i]] 
        else:
            sum_ += roman_map[s[i]]
    sum_ += roman_map[s[-1]]        
    return sum_           
s = "XXVI"
print(roman_to_int(s))
print(roman_to_int("IV"))

