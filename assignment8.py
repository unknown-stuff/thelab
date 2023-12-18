class TravelingSalesmanProblem:
def __init__(self, graph):
self.graph = graph
self.num_cities = len(graph)
self.memoization_table = {}
def tsp_dynamic_programming(self, mask, current_city):
#If all cities have been visited
if mask == (1 << self.num_cities) - 1:
return self.graph[current_city][0] # Return to the starting city
if (mask, current_city) in self.memoization_table:
return self.memoization_table[(mask, current_city)]
min_cost = float('inf')
# Try visiting each unvisited city
for next_city in range(self.num_cities):
if (mask >> next_city) & 1 == 0: # Check if the city has not been
visited
# Recursive call for the subproblem
cost = self.graph[current_city][next_city] +
self.tsp_dynamic_programming(
mask | (1 << next_city), next_city
)
min_cost = min(min_cost, cost)
# Memoize the result and return
self.memoization_table[(mask, current_city)] = min_cost
return min_cost
def solve_tsp(self):
return self.tsp_dynamic_programming(1, 0)
graph = [
[0, 12, 15, 20],
[12, 0, 5, 10],
[15, 5, 0, 8],
[20, 10, 8, 0]
]
tsp_solver = TravelingSalesmanProblem(graph)
min_cost = tsp_solver.solve_tsp()
print("Minimum Cost of TSP:", min_cost)
