### Reverse a list without using reverse() or slicing.
def reverse_list(l):
    start, end = 0, len(l) - 1
    while start <= end:
        l[start], l[end] = l[end], l[start]
        start, end = start + 1, end - 1
    return l

print(reverse_list([1, 2, 4, 6, 7]))    
