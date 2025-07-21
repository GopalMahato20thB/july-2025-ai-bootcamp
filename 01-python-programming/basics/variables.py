# Concept 01: Variables & Data Types 
"""
>>> Variable: container to store data in memory.
>>> Data Types: int, float, str, bool, list, tuple, set, dict, Nonetype
"""
name = "Gopal"
age = 19
height = 5.9
is_coder = True
skills = ["Python", "DSA"]
print(type(name), type(age), type(height), type(is_coder), type(skills))
print("--------------------------------------------")
print(f"Name: {name}, Age: {age}, height: {height}, Coder: {is_coder}, Skills: {skills}")

"""
Operators:
>>> Arithmetic: +, -, *, /, //, %, **
>>> Comparison: ==, !=, <, >, <=, >=
>>> Logical: and, or, not
>>> Assignment: =, +=, -=, etc.
>>> Identity: is, is not
>>> Membership: in, not in
"""
a = 10
b = 3
print(a ** b) #exponentiation
print( a > b and b != 0)

