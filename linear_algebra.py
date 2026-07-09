import numpy as np


def sumDiff(a, b):
    sum = a + b
    diff = a - b
    print(f"\na = \n{a}")
    print(f"\nb = \n{b}")
    print(f"\nsum = \n{sum}")
    print(f"\ndifference = \n{diff}")

#Problem 1
print("Problem 1:")
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
sumDiff(a, b)

#Problem 2
print("\n\nProblem 2:")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
sum = a + b
diff = a - b
print(f"\na = \n{a}")
print(f"\nb = \n{b}")
print(f"\nsum = \n{sum}")
print(f"\ndifference = \n{diff}")

#Problem 3
print("\n\nProblem 3:")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dotProduct = np.dot(a, b)
print(f"\na = {a}")
print(f"\nb = {b}")
print(f"\nDot product = {dotProduct}")

#Problem 4
print("\n\nProblem 4:")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
product = np.dot(a, b)
print(f"\na = \n{a}")
print(f"\nb = \n{b}")
print(f"\nproduct = \n{product}")

#Problem 5
print("\n\nProblem 5:")
a = np.array([1, 1, 2])
magnitude = np.linalg.norm(a)
print(f"\na = {a}")
print(f"\nmagnitude = {magnitude}")

#Problem 6
print("\n\nProblem 6:")
a = np.array([[1, 3], [2, 4]])
transpose = np.transpose(a)
print(f"\na = \n{a}")
print(f"\ntranspose = \n{transpose}")