"""
1. Creating a file named dairy.txt
2. Ask the user to input their daily task and write it to a diary.txt
3. Then read and print all tasks in the file.
"""
date = input("Date: ")
tasks = input(f"Thoughts on {date}!: ")
dairy_info = {}
dairy_info[date] = tasks
with open("dairy.txt", "a") as t:
    t.write(str(dairy_info))

user = input("Do you want to see the tasks(y/n):  ")
if user.lower() == "y":
    with open("dairy.txt", "r") as r:
        contents = r.read()
        print("Here is your all Tasks: ")
        print(contents)
print("Have a good day!")
