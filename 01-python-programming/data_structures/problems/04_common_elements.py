 ## Find common elements between two lists.
 
def common_elements(l1, l2):
    commons = []
    for i in l1:
        if i in l2:
            commons.append(i)
    return commons        

print(common_elements([1, 3, 5, 6, 9, 7], [7]))

