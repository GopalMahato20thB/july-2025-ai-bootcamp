# inheritance.py

# Base (parent) class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived (child) class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} says: Woof!")

    def display_breed(self):
        print(f"{self.name} is a {self.breed}.")

# Another derived class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

# Using the classes
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers")

print("Dog Object:")
dog1.speak()           # Overridden method
