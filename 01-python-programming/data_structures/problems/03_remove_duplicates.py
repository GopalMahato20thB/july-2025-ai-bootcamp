### Remove all duplicates from a list.

def remove_duplicates_list(l):
    unique_l = []
    for i in l:
        if i not in unique_l:
            unique_l.append(i)
    return unique_l

print(remove_duplicates_list([1, 3, 4, 5, 7, 7, 7, 9, 9]))

