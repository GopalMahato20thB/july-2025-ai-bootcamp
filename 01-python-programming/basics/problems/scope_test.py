## Show difference between local and global variables.

name = "Gopal Mahato"  # This is a global variable 
## it is accessable inside and outside the function

def is_consistent():
    #name = "Gopal" #it is accessable only inside the function
    return f"{name} is consistent!"
print(is_consistent())

