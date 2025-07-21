 ### From a list, return a new list of even numbers.
 
def filter_evens(l):
    return [i for i in l if i % 2 == 0]
print(filter_evens([1, 2, 4, 6, 7]))    
