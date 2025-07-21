## Practice Problems for basic/problems;
"""
1. name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, You are {age} years old!")
2. 
#type_checker.py: Input anything and print its type.
user_name = 19
print("Data Type: ", type(user_name))
3. #swap_variables.py: Swap values of two variables.
a = 1
b = 2
print(f"Original: a: {a},b: {b} ")
a, b = b, a
print(f"After swaping: a: {a}, b: {b}")
4. #area_calculator.py: Input radius, calculate area of circle.
user_input = float(input("Enter radius: "))
print("Area of circle is: ",3.14*user_input*user_input)
5. 
 compound_interest.py: Compute compound interest (P, R, T).  CI=P(1+i)^n −P
principal = 1000
rate = 0.05
time = 10
n = 12

amount = principal * (1 + rate / n) ** (n * time)
print(amount)
6. 
#calc_operators.py: Take two numbers, show all arithmetic operations.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Division: ", num1 / num2)
print("Integer Division: ", num1 // num2)
print("Modulo: ", num1 % num2)
print("Square: ", num1 ** num2)
#11. positive_negative.py: Check if a number is +, -, or 0.
num = int(input("Enter a number: "))

if num == 0:
    print(f"{num} is nor positive or negative\nThe Number aka {num} is Zero")
if num > 0:
    print(f"{num} is positive") 
if num < 0:
    print(f"{num} is negative"
12.
#12. grade_checker.py: Assign grades based on marks.
student_name = input("Enter Your name: ")
student_marks = float(input("Enter your marks: "))

if student_marks < 50:
    print(f"{student_name}: FAILED!") 
if student_marks >= 50 and student_marks < 60:
    print(f"{student_name}: D ")
if student_marks >= 60 and student_marks < 70:
    print(f"{student_name}: C ")
if student_marks >= 70 and student_marks < 80:
    print(f"{student_name}: B ") 
if student_marks >= 80 and student_marks < 90:
    print(f"{student_name}: A ")    
if student_marks >= 90 and student_marks <= 100:
    print(f"{student_name}: AA ")
13. 
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, " is FizzBuzz!")
    elif i % 3 == 0:
        print(i, " is Fizz")
    elif i % 5 == 0:
        print(i, " is Buzz")
    else:
        print(i, f" {i}")
 
14. 
# sum_even_numbers.py: Sum all even numbers from 1 to N.
n = int(input("How many numbers?: "))

sum_of_evens = 0
for i in range(n):
    if i % 2 == 0:
        sum_of_evens += i

print(sum_of_evens)
15. 
#factorial_while.py: Calculate factorial using while loop.

num = int(input("Enter a number to know factorial of: "))

factorial = 1
while num != 0:
    factorial *= num
    num -= 1

print(factorial)  

16. 
# Write a function to check prime number
def is_prime(n):    
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

print(is_prime(7))
print(is_prime(9))
print(is_prime(11))
print(is_prime(99))
17. 
## Write a function that calculates x^n.
def square(x, n):
    return x**n

print(square(5, 3))   
18.
reverse a string using functions.
### Reverse a string using functions

def reverse_string(s):
    reverse_string = ""
    for i in range(len(s) - 1, -1, -1):
        reverse_string += s[i]
    return reverse_string   

print(reverse_string("Gopal"))
print(reverse_string("mam"))

19.
##Return n-th Fibonacci number.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end= " ")
print()    
20.
## Show difference between local and global variables.

name = "Gopal Mahato"  # This is a global variable 
## it is accessable inside and outside the function

def is_consistent():
    #name = "Gopal" #it is accessable only inside the function
    return f"{name} is consistent!"
print(is_consistent())



"""
