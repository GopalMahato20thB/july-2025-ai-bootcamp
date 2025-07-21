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
"""
