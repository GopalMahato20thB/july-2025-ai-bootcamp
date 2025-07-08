# STEP 1. Linear Algebra Basics (Vectors & Matrices)
# 1.1 What is vector?
# A vector is a 1D array of numbers.
# Can be row and column format.
import numpy as np
"""
v = np.array([2, 3, 5]) #1D vector

#What is Matrix?

#A matrix is a 2D array (rows x columns).
A = np.array([[1, 2], [3, 4], [5, 6], [9, 10], [100, 10002]]) # 2 x 2 matrix

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# numpy performs operations element by element
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# array with Scalar, Scalar applies to all elements (brodcasting).
print("Original Numpy array a: ",a)
print("After adding 10", a + 10)
print("After adding 2", a + 2)
print("--------------------------")
#step5 usefull operations
print(np.sum(a))
print(np.prod(a))
print(np.mean(a))
print(np.std(a)) # standard division
print(np.max(a))
print(np.min(a))
print(np.argmax(a))  # index of max
"""

"""
#Reshaping  arrays 
a2 = np.array([[1, 2, 3], [4, 5, 6]])  # shape: (2, 3) first argument is the number of row and second one is the number column
print(a2.shape) 
print(a2.reshape(3, 2)) #change to 3 rows, 2 cols
print("---"* 10)
print(a2)
print("---"* 10)

# Slicing Arrays
a = np.array([10, 20, 30, 40, 50])
print(a[1:4]) #if i use basic rules of slicing an array the answer must be 20 30 40 I am completly right
print(a[::-1])  # if i follow basic list or array rules then the answer must be reverse

print("----"* 10)

# here is one very important topic: Broadcasting
m = np.array([[1 ,2], [3, 4]])
v = np.array([10, 20])
print(m + v) # [[11 22] [13 24]]
print("-broder--"*5)
print(v + m) 
# here vector v is added to every row of matrix m.
"""

### Practice questons
#Q1: Element-wise Operations
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 3, 5])

result = (arr1 * arr2) + (arr1 - arr2) #lets predicts the answer: 
prediction = [3, 13, 31]
print(result == prediction)

#Q2: Reshaping and Slicing
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
#print the second row in reverse
print(arr[1][::-1])  # it will print [60, 50, 40]

#Q3: Broadcasting 
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 100])
result2 = A + B # 
prediction2 = [[11, 102], [13, 104]]
print(result2 == prediction2)





 


