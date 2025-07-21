#factorial_while.py: Calculate factorial using while loop.

num = int(input("Enter a number to know factorial of: "))

factorial = 1
while num != 0:
    factorial *= num
    num -= 1

print(factorial)    

