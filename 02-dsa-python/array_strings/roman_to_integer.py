"""
Given a string s representing a Roman numeral, convert it to an integer.

🧠 Roman Numeral Basics:
Symbol	Value
I	      1
V	      5
X	      10
L	      50
C         100
D       	  500
M	      1000

Special Subtraction Cases:

IV = 4 (5 - 1)
IX = 9 (10 - 1)
XL = 40 (50 - 10)
XC = 90 (100 - 10)
CD = 400 (500 - 100)
CM = 900 (1000 - 100)
"""

### Logic is: If current symbol value < next symbol value, Then I need to subtract that. else add that

def roman_to_int(s):
    roman = {
        "I": 1, "V": 5, "X": 10, "L": 50, 
        "C": 100, "D": 500, "M": 1000
    }
    total = 0
    previous = 0
    for char in reversed(s):
        value = roman[char]
        if value < previous:
            total -= value
        else:
            total += value
        previous = value
    return total

print(roman_to_int("III"))
print(roman_to_int("IX"))
print(roman_to_int("MMIIIIII"))
