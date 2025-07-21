# Reading from a file
with open("test.txt", "r") as f:
    print("First 10 characters:", f.read(10))
    f.seek(0)  # Move to start
    for line in f:
        print("Line:", line.strip())
