 #Merge two lists and return a sorted list without duplicates.
 
def merge_and_sort(l1, l2):    
    return sorted(set(l1 + l2))
print(merge_and_sort([1, 3, 5, 7],[2, 3, 6, 7, 8]))
