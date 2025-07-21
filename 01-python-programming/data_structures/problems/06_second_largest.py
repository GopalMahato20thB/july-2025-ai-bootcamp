## Find the second largest number in a list.

def second_largest(l):  
    max_value = float("-inf")
    second_max = float("-inf")
    for i in l:
        if i > max_value:
            second_max = max_value
            max_value = i
        elif max_value > second_max > i:
            second_max = i
    return second_max if second_max != float("-inf") else None        
            
print(second_largest([1, 3, 4, 7]))            
