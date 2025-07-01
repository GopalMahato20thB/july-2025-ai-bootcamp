## starting from the basics
"""
# 1. Variables, Data Types, and Operators
# Variables: Variables are names used to store data values.
x = 10  # interger
name = "Gopal" #string
pi = 3.14 #float
#Python is dynamically typed, so you don't need to declare types explicitly.
# Data types: Common types
# int - Whole numbers (5, -1, -2, 0)
# float - Decimal numbers (3.14, 78.82)
# str - Text ("Hello", "Gopal", "AI Architect")
# bool - Boolean (True, False)
# list, tuple, dict, set (I'll cover them later)
print(type(5))
print("------"* 16)
#operators 
# Arithmetic +, -, *, /, //, %, **
# Comparison: ==, !=, >, <, >, >=, <= 
# Assignment: =, +=, -=, etc.
num1 = 5
num2 = 2
print(num1 + num2) # 7
print(num1 // num2) # 2
print(num1 % num2)  # 1
print(num1 ** num2)  # 25 power
print(6 ** 3) # this must return 216
print("----" * 10)

# Input and output operations
# input:
name = input("Enter your name: ")
age = int(input("Enter your age: ")) # converting input to interger

print("Hello", name)
print(f"You are {age} years old") # f-string formating

print("-----" *  7)
"""
'''
# 3. Basic string Operations
text = "AI Architect"
print(text[0]) #prints A
print(text[-1]) # t
print(len(text)) # 12 if spaces are include(after i run this program it is)

# slicing
print(text[3:13]) #Architect
print(text[:2]) # AI
print(text[3:]) # Architect

# methods
print(text.lower()) # ai architect
print(text.upper()) # AI ARCHITECT
print(text.replace("Architect", "Engineer")) # AI Engineer
print("AI" in text) # True
print("Engineer" in text) # False
'''
print("---" * 16)
# Practice checkpoints: Before I move to DSA problems, try answering this
# 1. 
a = 15
b = 4 
print(a / b) # 3.75
print(a // b) # 3

# 2. Taking user's name and age as input 
# and printing Hello [name], you will be [age + 1] next year.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you will be {age + 1} next year.")





