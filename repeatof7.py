class Knapsack_problem:
def __init__(self, weights, values, capacity):
self.weights = weights
self.values = values
self.capacity = capacity
self.n = len(weights)
# Create a dynamic programming table
self.dp_table = [[0] * (capacity + 1) for _ in range(self.n + 1)]
# List to store selected items
self.selected_items = []
def solve_knapsack(self):
for i in range(1, self.n + 1):
for w in range(self.capacity + 1):
if self.weights[i - 1] <= w:
# Choose the maximum value between including or excluding
the current item
self.dp_table[i][w] = max(
self.values[i - 1] + self.dp_table[i - 1][w -
self.weights[i - 1]],
self.dp_table[i - 1][w]
)
else:
# If the current item's weight exceeds the remaining
capacity, skip it
self.dp_table[i][w] = self.dp_table[i - 1][w]
# Backtrack to find the selected items
i, w = self.n, self.capacity
while i > 0 and w > 0:
if self.dp_table[i][w] != self.dp_table[i - 1][w]:
self.selected_items.append(i - 1)
w -= self.weights[i - 1]
i -= 1
def get_result(self):
# Get the maximum profit and the list of selected items
max_profit = self.dp_table[self.n][self.capacity]
return max_profit, self.selected_items
weights = [1, 2, 3, 4]
values = [5, 7, 2, 8]
capacity = 5
knapsack_solver = Knapsack_problem(weights, values, capacity)
knapsack_solver.solve_knapsack()
max_profit, selected_items = knapsack_solver.get_result()
print("Maximum Profit:", max_profit)
print("Selected Items:", selected_items)
