"""
Task
1. Ask the user to enter two numbers.
2. Divide the first by the second.
3. Handle:
    >Division by zero
    >Invalid input(e.g. letters instead of numbers)
"""
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the Second number: "))
    print(num1 / num2)
except ZeroDivisionError:
    print(f"{num1} can't divide by zero!")

except ValueError:
    print("Invalid number!, Enter a valid number!")

finally:
    print("The try block is finished!")


