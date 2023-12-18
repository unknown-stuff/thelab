class EightQueens:
def __init__(self, board_size):
# Initialize the class with the board size and an empty list to store
solutions
self.board_size = board_size
self.solutions = []
def is_safe(self, board, row, col):
# Check if placing a queen at a given position is safe
for prev_row in range(row):
prev_col = board[prev_row]
if prev_col == col or \
prev_col - prev_row == col - row or \
prev_col + prev_row == col + row:
return False
return True
def solve_queens(self, board, row):
# Recursive function to find solutions using backtracking
if row == self.board_size:
# If all queens are placed, store the current solution
self.solutions.append(board.copy())
return
for col in range(self.board_size):
if self.is_safe(board, row, col):
board[row] = col
self.solve_queens(board, row + 1)
def find_solutions(self):
# Initialize the board with -1 and start the backtracking process
board = [-1] * self.board_size
self.solve_queens(board, 0)
def print_solutions(self):
for solution in self.solutions:
for col in solution:
line = ''.join(['Q ' if c == col else '. ' for c in
range(self.board_size)])
print(line)
print()
board_size = 8
eight_queens_solver = EightQueens(board_size)
eight_queens_solver.find_solutions()
eight_queens_solver.print_solutions()
