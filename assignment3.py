import numpy as np # Importing the numpy library for array operations
class StrassenMatrixMultiply:
def __init__(self, matrix1, matrix2):
# Initializing the class with the input matrices
self.matrix1 = matrix1
self.matrix2 = matrix2
def split_matrix(self, matrix):
# Function to split a given matrix into four submatrices
if matrix.shape[0] % 2 != 0 or matrix.shape[1] % 2 != 0:
raise ValueError("Matrix dimensions must be even for 
Strassen's algorithm.")
row, col = matrix.shape
row2, col2 = row // 2, col // 2
return matrix[:row2, :col2], matrix[:row2, col2:], 
matrix[row2:, :col2], matrix[row2:, col2:]
def strassen_multiply(self, matrix1, matrix2):
# Base case for when the matrices are of size 1x1
if len(matrix1) == 1:
return matrix1 * matrix2
# Splitting the matrices into submatrices
a, b, c, d = self.split_matrix(matrix1)
e, f, g, h = self.split_matrix(matrix2)
# Applying Strassen's algorithm for matrix multiplication
p1 = self.strassen_multiply(a, f - h)
p2 = self.strassen_multiply(a + b, h)
p3 = self.strassen_multiply(c + d, e)
p4 = self.strassen_multiply(d, g - e)
p5 = self.strassen_multiply(a + d, e + h)
p6 = self.strassen_multiply(b - d, g + h)
p7 = self.strassen_multiply(a - c, e + f)
# Calculating the submatrices of the resulting matrix
result = np.zeros(matrix1.shape)
result[: len(result) // 2, : len(result) // 2] = p5 + p4 - p2 + 
p6
result[: len(result) // 2, len(result) // 2:] = p1 + p2
result[len(result) // 2:, : len(result) // 2] = p3 + p4
result[len(result) // 2:, len(result) // 2:] = p1 + p5 - p3 -
p7
return result
# Example usage:
try:
# Defining the matrices with even dimensions
matrix1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 
[13, 14, 15, 16]])
matrix2 = np.array([[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 
5], [4, 3, 2, 1]])
# Creating an instance of the StrassenMatrixMultiply class
strassen_multiply = StrassenMatrixMultiply(matrix1, matrix2)
# Performing Strassen's matrix multiplication on the given matrices
result = strassen_multiply.strassen_multiply(matrix1, matrix2)
# Printing the original matrices and the result of the 
multiplication
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResult after Strassen's matrix multiplication:")
print(result)
except ValueError as e:
print(f"ValueError: {e}")
except Exception as e:
print(f"An error occurred: {e}")
