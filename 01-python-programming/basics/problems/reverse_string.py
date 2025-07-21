### Reverse a string using functions

def reverse_string(s):
    reverse_string = ""
    for i in range(len(s) - 1, -1, -1):
        reverse_string += s[i]
    return reverse_string   

print(reverse_string("Gopal"))
print(reverse_string("mam"))
        
        
