class Matrix:
def __init__(self, rows, cols):
self.rows = rows
self.cols = cols
self.data = [[0 for _ in range(cols)] for _ in range(rows)]
def input_matrix(self):
print(f"Enter {self.rows}x{self.cols} matrix elements:")
for i in range(self.rows):
row = input().split()
if len(row) != self.cols:
raise ValueError("Invalid input. Each row should contain exactly the same number of elements.")
for j in range(self.cols):
self.data[i][j] = int(row[j])
def display_matrix(self):
print("Matrix:")
for row in self.data:
print(*row)
def transpose(self):
transposed = Matrix(self.cols, self.rows)
for i in range(self.rows):
for j in range(self.cols):
transposed.data[j][i] = self.data[i][j]
return transposed
def add(self, other):
if self.rows != other.rows or self.cols != other.cols:
raise ValueError("Matrix dimensions do not match for addition.")
result = Matrix(self.rows, self.cols)
for i in range(self.rows):
for j in range(self.cols):
result.data[i][j] = self.data[i][j] + other.data[i][j]
return result
def subtract(self, other):
if self.rows != other.rows or self.cols != other.cols:
raise ValueError("Matrix dimensions do not match for 
subtraction.")
result = Matrix(self.rows, self.cols)
for i in range(self.rows):
for j in range(self.cols):
result.data[i][j] = self.data[i][j] - other.data[i][j]
return result
def multiply(self, other):
if self.cols != other.rows:
raise ValueError("Matrix dimensions are not compatible for 
multiplication.")
result = Matrix(self.rows, other.cols)
for i in range(self.rows):
for j in range(other.cols):
for k in range(self.cols):
result.data[i][j] += self.data[i][k] * other.data[k][j]
return result
def divide(self, other):
if self.rows != other.rows or self.cols != other.cols:
raise ValueError("Matrix dimensions do not match for division.")
result = Matrix(self.rows, self.cols)
for i in range(self.rows):
for j in range(self.cols):
if other.data[i][j] == 0:
raise ValueError("Division by zero is not allowed.")
result.data[i][j] = self.data[i][j] / other.data[i][j]
return result
if __name__ == "__main__":
print("Matrix 1:")
m1 = int(input("Enter the number of rows for matrix1: "))
n1 = int(input("Enter the number of columns for matrix1: "))
matrix1 = Matrix(m1, n1)
matrix1.input_matrix()
print("Matrix 2:")
m2 = int(input("Enter the number of rows for matrix2: "))
n2 = int(input("Enter the number of columns for matrix2: "))
matrix2 = Matrix(m2, n2)
matrix2.input_matrix()
print("\nMatrix 1:")
matrix1.display_matrix()
print("\nMatrix 2:")
matrix2.display_matrix()
try:
transposed1 = matrix1.transpose()
print("\nTranspose of matrix1:")
transposed1.display_matrix()
transposed2 = matrix2.transpose()
print("\nTranspose of matrix2:")
transposed2.display_matrix()
except ValueError as e:
print(str(e))
try:
print("\nPerform addition of matrix1 with matrix2:")
added = matrix1.add(matrix2)
added.display_matrix()
except ValueError as e:
print(str(e))
try:
print("\nPerform subtraction of matrix1 from matrix2:")
subtracted = matrix2.subtract(matrix1)
subtracted.display_matrix()
except ValueError as e:
print(str(e))
try:
print("\nPerform multiplication of matrix1 and matrix2:")
multiplied = matrix1.multiply(matrix2)
multiplied.display_matrix()
except ValueError as e:
print(str(e))
try:
print("\nPerform division of matrix1 by matrix2:")
divided = matrix1.divide(matrix2)
divided.display_matrix()
except ZeroDivisionError as e:
print("Division by zero is not allowed.")
except ValueError as e:
print(str(e))
