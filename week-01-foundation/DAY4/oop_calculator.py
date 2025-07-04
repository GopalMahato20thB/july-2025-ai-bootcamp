"""
🛠️ Your Task: Build a Calculator Class
Create a class Calculator with the following:
Attributes:
None needed for now (stateless calculator)
Methods:
1. add(a, b) → returns a + b
2. subtract(a, b) → returns a - b
3. multiply(a, b) → returns a * b
4. divide(a, b) → returns a / b (handle divide by zero)
✅ Bonus (if you want to try):
Add a method power(a, b) → returns a ** b
Add a method modulo(a, b) → returns a % b
"""

class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    #methods
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        if self.b == 0:
            print("Can't divisible by zero!")  
        else:
            return self.a / self.b
    def power(self):
        return self.a ** self.b
    
    def modulo(self):
        return self.a % self.b


test1 = Calculator(4, 5)         
print(test1.power())
print(test1.add())        
