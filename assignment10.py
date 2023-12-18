class GraphColoring:
def __init__(self, graph):
self.graph = graph
self.num_vertices = len(graph)
self.colors = [0] * self.num_vertices
def is_safe(self, vertex, color):
# Check if it's safe to assign the given color to the vertex.
for neighbor in self.graph[vertex]:
if self.colors[neighbor] == color:
return False
return True
def graph_coloring(self, num_colors, vertex=0):
# Recursive function to find a valid coloring for the graph.
if vertex == self.num_vertices:
# If all vertices are colored, a solution is found.
return True
for color in range(1, num_colors + 1):
if self.is_safe(vertex, color):
# If it's safe to assign the color, do so.
self.colors[vertex] = color
if self.graph_coloring(num_colors, vertex + 1):
return True
# Backtrack if the current assignment does not lead to a
solution.
self.colors[vertex] = 0
return False # If no color assignment leads to a solution, return
False.
graph = {
0: [1, 2, 3],
1: [0, 2],
2: [0, 1, 3],
3: [0, 2]
}
num_colors = 3
graph_coloring_instance = GraphColoring(graph)
if graph_coloring_instance.graph_coloring(num_colors):
print("Graph Coloring:")
for i in range(graph_coloring_instance.num_vertices):
print(f"Vertex {i + 1}: Color {graph_coloring_instance.colors[i]}")
else:
print("Solution does not exist.")
