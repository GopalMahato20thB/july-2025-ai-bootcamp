#11. positive_negative.py: Check if a number is +, -, or 0.
num = int(input("Enter a number: "))

if num == 0:
    print(f"{num} is nor positive or negative\nThe Number aka {num} is Zero")
if num > 0:
    print(f"{num} is positive") 
if num < 0:
    print(f"{num} is negative")
    
