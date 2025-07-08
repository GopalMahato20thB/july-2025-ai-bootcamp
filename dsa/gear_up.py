"""PARTONE
## gear up 
#example task 01
a = 5
b = "10"
result1 = a + int(b) 
prediction1 = 5 + 10
print(result1 == prediction1)

## example task 02
a1 = 5 
b1 = 2
result2 = a1 > b1 and a1 % 2 == 1 
prediction2 = True 
print(result2 == prediction2)

##  example functions
def add1(a, b):
    return a + b
result3 = add1(3, 4)
prediction3 = 7
print(result3 == prediction3)

print("-" * 10)
## example etc
d1 = {"a": 1, "b": 2} 
result4 = d1["a"]
prediction4 = 1
print(result4 == prediction4)

s1 = set([1, 2, 2, 3])
result5 = s1
prediction5 = {1, 2, 3} ## it can be false because sets are unordered
print(result5 == prediction5)
"""

"""PART-TWO
#####################################################
### part 2 task 1
aa = 10
bb = "20"
cc = 2.5
## convert b to integer and add all three 
## expected Output 32.5
print(aa + int(bb) + cc)
#DONE

# task 2: Create a list of 4 values of different types (int, float, bool), and print each one with its type().
num_fav = 7
aim_love = 100.00
is_consistent = True
aim = "AI Architect"
print(type(num_fav), type(aim_love), type(is_consistent), type(aim))

# task3 
xx = 10
yy = 3
# divide xx by yy and print the result as float, integer(floor division), remainder (modulus)

print(f"float division: {float(xx / yy)} | integer (floor division): {int(xx / yy)} | remainder(modulus): {xx % yy}")
"""


######################################################

"""PART-THREE
### task 01 
aaa, bbb = 11, 4
print(aaa / bbb)
print(int(aaa / bbb))
print(aaa ** bbb)
print(aaa % bbb)

### task 02: 
age = 19
has_id = True
#check if the person is allowed to vote (age >= 18 and has id)
if age >= 18 and has_id == True:
    print("He can")

    
#### task 03: True or Flase
print("-----------------------"*2)
xxxx = 5
yyyy = 8

print(xxxx > 3 and yyyy < 10) ## must True
print(xxxx == yyyy or xxxx < yyyy) ## can be true 
print(not(xxxx > yyyy))  ## must True
"""

####################################################

"""PART-FOUR
## task 01 
x = 1 
# write a program that:
# prints "Even" if x is even
# prints "Odd" if x is odd

if x % 2 == 0:
    print("Even")
if x % 2 != 0:
    print("Odd")
    

## task 02
temp = 25
# if temperature > 30: print "hot" 
# if 20 <= temperature <= 30: print "Normal"
# else print cold

if temp > 30:
    print("Hot")
elif temp >= 20 and temp <= 30:
    print("Normal")
else:
    print("Cold")

## task 03 
char = "O"
vowels = "aeiou"
if char.lower() in vowels:
    print(char," is a vowel!")
"""

##################################################

""""PART-FIVE
## task 01: print squares of numbers from 1 to 10
for number in range(1, 11):
    print(number * number, end=" ")
print()

## task 02: Reverse a number using while loop
# input: 123 output 321
num = 123

result = 0

while num != 0:
    digit = num % 10
    num = num // 10
    result = result * 10 + digit
print("Reversed: ", result)

### task 03: Count vowels in a string

string = "education"
all_vowels = "aeiou"
count = 0
for s in string.lower():
    if s in all_vowels:
        count += 1
print(count)        
"""


"""PART-SIX
### task 01: Reverse string

string = "python"
print(string[::-1])


## task 02: Counting how many times "e" appears in a string 

value = "e"
example_string = "experience"

count_value = 0
for s in example_string:
    if s == value:
        count_value += 1
print(count_value)

#### task 03: Check if input is a numeric string
string1 = "1234"
if string1.isdigit():
    print("True")
else:
    print("False")

### task 04: Return the last word of a sentence
name = "My name is Gopal Mahato"

last_name = name.split()
print(last_name[-1])
"""

"""PART-SAVEN
### task 01: Sum of even numbers from list 
nums = [1, 2, 3, 4, 5, 6, 7]

sum_ = 0
for num in nums:
    if num % 2 == 0:
        sum_ += num
print(sum_)


#### task 02: reverse a list without using [::-1] 

nums.reverse()
print(nums)
print("------" * 12)
def reverse_list(arr):
    start, end = 0, len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end - 1
    return arr

print(reverse_list([1, 3, 3, 7]))

### task 03 Remove duplicates from a list
nums = [1, 2, 2, 3, 4, 4, 5]
without_duplicates = list(set(nums))
print(without_duplicates)

### task 04: sort a list in descending order 
nums1 = [3, 1, 4, 2]
nums1.sort()
print(reverse_list(nums1))
"""

### task 01: Write a function to check if a number is even

def is_even(num):
    return num % 2 == 0

print(is_even(7))
print(is_even(0))
print(is_even(10))

### task 02: Write a function that returns factorial of a number

def factorial(num): 
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
print(factorial(7))
print(factorial(5))

#### task 03: Write a function that takes a list and returns the maximum value

def find_max(nums): 
    return max(nums)

print(find_max([1, 2, 3, 4, 5]))

def find_max2(nums):
    max_ = 0 
    for num in nums:
        if num > max_:
            max_ = num
    return max_        
print(find_max2([1, 3, 6, 7]))


 








