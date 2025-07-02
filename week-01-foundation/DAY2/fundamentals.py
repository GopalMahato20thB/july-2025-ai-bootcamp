"""
# 1. Checking prime number or not
def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")

is_prime(7)
is_prime(9)
is_prime(11)
is_prime(1)
is_prime(6)

print("----" * 13)

print("-----" * 10)


#pyramin pattern

"""

"""
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

print(factorial(5))     

def palindrome(string):
    string = string.lower()
    return string == string[::-1]

print(palindrome("Gopal"))
print(palindrome("madam"))
## observing global variables

name = "Gopal Mahato" # global variable

def greet():
    friends_name = "Abhijit"
    print("Hello", name)
    print(friends_name, "is my one of my friend!")
    return "Nothing"
    
print(greet())
"""
# 8. Function that returns the sum, product, and average
"""
def compute_stats(numbers):
    store_data = []
    product = 1
    for i in range(numbers):
        num = float(input("Enter a number: "))
        store_data.append(num)
        product *= num
    
    sum_ = sum(store_data)
    average = sum_ / numbers
    return sum_, product, average

print(compute_stats(4))

print("---" * 16)

"""
"""
##### Rotate a list to the right by k steps
#input: [1,2,3,4,5] output: [4,5,1,2,3]
# first i will reverse then reverse k position first then others element
def reverse_list(start, end, arr):    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end  -  1
    return arr


def rotate_list(arr, k):    
    n = len(arr)
    k = k % n
    reverse_list(0, n - 1, arr)
    reverse_list(0, k - 1 , arr)
    reverse_list(k, n - 1, arr)
    return arr

print(rotate_list([1,2,3,4,5], 2))


### finding the second largest in a list
def find_second_max(arr):
    return sorted(arr)[-2]
print(find_second_max([12,32,7,74,2,13]))

### 12. Counting Even and Odd numbers in a list

def count_EvenOdd(arr):
    total_evens = 0
    total_odds = 0
    for num in arr:
        if num % 2 == 0:
            total_evens += 1
        if num % 2 != 0:
            total_odds += 1
            
    print("Evens: ", total_evens)
    print("Odds: ", total_odds)
    return "I return nothing form this function"    
print(count_EvenOdd([1,2,3,4,5,6,7])) 
"""
# Count Vowels and Consonant in a string
def count_vc(string):
    vowels = "aeiou"
    consonants = "qwrtypsdfghjklzxcvbnm"
    count_vowels = 0
    count_consonants = 0
    
    for s in string.lower():
        if s in vowels:
            count_vowels += 1
        if s in consonants:
            count_consonants += 1
    return count_vowels, count_consonants
print(count_vc("AI Architect"))

#pyramid pattern 
def pyramid_main(rows):	
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

pyramid_main(7)

# remove duplicates
def removeDuplicates(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

# I know its use extra space

print(removeDuplicates([1,2,3,4,5,6,7,8,7]))
            
#### sum of odd and evens
'''
evens = sum(1 for x in arr if x % 2 == 0)
is equivalent to 
evens = 0
for x in arr:
    if x % 2 == 0:
        evens += 1
'''
def count_even_odd(arr):
    evens = sum(1 for x in arr if x % 2 == 0)
    odds = len(arr) - evens
    return evens, odds
print(count_even_odd([1,2,3,4,5,6,7]))


# fibonacci sequence 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(5)

