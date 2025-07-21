##13.  fizz_buzz.py: Classic FizzBuzz (1 to 50).
"""
FizzBuzz Python:
The FizzBuzz problem is a classic programming challenge often used in interviews to test basic programming skills. The task is to write a program that prints the numbers from 1 to 100, with specific replacements for multiples of 3 and 5. 
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, " is FizzBuzz!")
    elif i % 3 == 0:
        print(i, " is Fizz")
    elif i % 5 == 0:
        print(i, " is Buzz")
    else:
        print(i, f" {i}")
        
