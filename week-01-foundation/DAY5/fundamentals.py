"""
File I/O (Input/Output) allows python Program to read from and write to files on computer.
""" 
#Here is some basic operations
# open a file: open(filename, mode)
# Modes:
# "r": read, "w": write(overwrites), "a": append, "rb", "wb": read/write in binary
## read from file: .read(), .readline(), .readlines()
## write to a file: .write(), .writelines()
### writing to a file 
"""
with open("gopal.txt", "w") as f:
    f.write("My name is Gopal Mahato!\nI am learning concepts and practicing File I/O")

## Reading from a file
with open("gopal.txt", "r") as f:
    contents = f.read()
    print(contents)
"""


"""
# 2. Exception Handling 
# Sometimes program might crash due to errors like dividing by zero or reading a file that doesn't exists.

## Exception handling allows to catch these errors and and handle the, gracefully using: try, except, finally(optional), else (optional)
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result: ",result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid Input! Enter a valid number!")
finally:
    print("try block is finished!")
"""

"""
Modules: 
A module is just a .py file containing functions, variables, or classes you can reuse in other files.
I can use:
    >Import built-in modules: import math, import random, import time
    >Create own modules and import them


What are Packages?
A package is a folder that contains multiple .py files (modules) and an __init__.py file (can be empty).
Used to origanize related code.    
"""
#example of math module
import math
print("Square root of 25 is: ", math.sqrt(25))