#4. Functions & Scope
"""
Function declaration and return
Parameters and arguments
global, local variables
Recursion (e.g., factorial, Fibonacci)
"""
def greet(name):
    return f"Hello, {name}!"
print(greet("Gopal"))

#recursion example

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(5))



