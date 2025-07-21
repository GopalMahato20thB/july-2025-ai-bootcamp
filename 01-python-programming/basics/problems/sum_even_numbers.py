# sum_even_numbers.py: Sum all even numbers from 1 to N.
n = int(input("How many numbers?: "))

sum_of_evens = 0
for i in range(n):
    if i % 2 == 0:
        sum_of_evens += i

print(sum_of_evens)

