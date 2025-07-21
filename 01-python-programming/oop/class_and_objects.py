

# Define a simple class to represent a student
class Student:
    # Constructor (initializer) method
    def __init__(self, name, roll_no, marks):
        self.name = name            # Instance variable for name
        self.roll_no = roll_no      # Instance variable for roll no
        self.marks = marks          # Instance variable for marks

    # Method to display student details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    # Method to check if student passed
    def is_pass(self):
        return self.marks >= 40

# Create objects (instances) of Student class
student1 = Student("Alice", 101, 85)
student2 = Student("Bob", 102, 37)

print("Details of Student 1:")
student1.display_details()
print("Passed:", student1.is_pass())

print("\nDetails of Student 2:")
student2.display_details()
print("Passed:", student2.is_pass())

# Demonstrating how to access and update attributes from outside the class
student2.marks = 42
print("\nAfter updating marks of Student 2:")
student2.display_details()
print("Passed:", student2.is_pass())
