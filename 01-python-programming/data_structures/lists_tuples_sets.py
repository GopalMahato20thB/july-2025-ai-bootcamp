## 1. LISTS in Python
"""
📘 What is a List?
A list is an ordered, mutable collection of items. You can add, remove, and change elements.
"""
fruits = ["apple", "banana", "mango"]
print(fruits[1]) #accessing 2nd element

numbers = [10, 20, 30, 40]

# Access
print(numbers[0])      # 10
print(numbers[-1])     # 40

# Modify
numbers[1] = 99
print(numbers)         # [10, 99, 30, 40]

# Add
numbers.append(50)
numbers.insert(2, 25)
print(numbers)         # [10, 99, 25, 30, 40, 50]

# Delete
numbers.remove(99)
del numbers[0]
print(numbers)         # [25, 30, 40, 50]

# Slice
print(numbers[1:3])    # [30, 40]

# Loop
for n in numbers:
    print(n)

# Membership
print(30 in numbers)   # True

# Sorting
numbers.sort()
print(numbers)

# Reversing
numbers.reverse()
print(numbers)

