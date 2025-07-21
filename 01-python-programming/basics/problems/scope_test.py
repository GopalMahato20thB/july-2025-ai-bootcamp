## Show difference between local and global variables.
name = "Gopal"  # global

def change_name():
    name = "AI Engineer"  # local
    print("Inside function:", name)

change_name()
print("Outside function:", name)


