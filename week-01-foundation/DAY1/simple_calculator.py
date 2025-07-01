# Project: Simple Calcultor
'''
Build a calculator that:
Takes two numbers from the user
Asks for an operation: +, -, *, /
Peforms and prints the result
'''
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
choice = input("Choose operation ( +, -, *, /): ")
if choice == "+":
    print("Result: ", first_num + second_num)
elif choice == "-":
    print("Result: ", first_num - second_num)
elif choice == "*":
    print("Result: ", first_num * second_num)
elif choice == "/":
    if second_num == 0:
        print("Can't divisible by zero")
    else:
        print("Result: ", first_num / second_num)
else:
    print("Invalid Choice")
    
    
