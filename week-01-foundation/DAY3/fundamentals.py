'''
1. List, Tuples, and Sets
> List: Ordered, mutable, allows duplicates. Example: [1, 2, 3]
> Tuple: Ordered, immutable, allows duplicates. Examples: (1, 1, 3, 7)
> Set: Unordered, mutable, no duplicates. Example: {1,2,3}
'''
#task1
def analyze_sequence(data):
    if not data:
        print("Its an empty list")
        
    else:
        unique_elements = set(data)
        small_element = min(data)
        sum_of_elements = sum(data)
        tuple_version = tuple(data)
        return unique_elements, small_element, sum_of_elements, tuple_version
    return None    

data = [1, 2, 7, 9, 3, 7, 1, 2]
print(analyze_sequence(data))
print(analyze_sequence([]))

"""
2. Dictionary Operations
Quick Summary:
A dictionary stores data in key-value pairs.
like this 
person = {"name": "Gopal", "age": 19}
adding new key
person["city"] = "Purulia"
"""
#task2 
def update_inventory(inventory, item, qty):
    if qty < 0:
        print("Can't be negative")
        return inventory
    else:
    
        if item in inventory:
            inventory[item] += qty
        else:
            inventory[item] = qty
    return inventory

inventory = {"banana": 6, "apple": 3, "chicken": 1}
item = "chicken"
qty = 1

print(update_inventory(inventory, item, qty))
print(update_inventory({}, "mango", 1))
print(update_inventory({}, "mango", -1))


"""
3. List Comprehensions
Quick Summary:
List comprehension is a concise way to create lists:
like this:
squares = [x**2 for x in range(5)]
"""
# Task3
evens = [x*x for x in range(50) if (x % 2 == 0 and x % 3 == 0)]
print( evens)
