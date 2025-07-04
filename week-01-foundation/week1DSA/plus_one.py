"""
🧠 LeetCode 66 – Plus One
📜 Problem Statement:
You are given a large integer represented as an array of digits, where:
Each element digits[i] is a single digit (0–9)
The most significant digit is at the front of the list (index 0)
🔸 Add 1 to this number and return the resulting number as a list of digits
"""
def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits     

print(plus_one([1, 2, 2]))    
print(plus_one([1, 2, 9]))    
            
            
