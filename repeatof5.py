Class Graph:
def __init__(self):
self.nodes = set()
self.edges = {}
# Initialize an empty dictionary to store distances between nodes
self.distances = {}
def add_node(self, value):
self.nodes.add(value)
def add_edge(self, from_node, to_node, distance):
# Check if from_node is already in the edges dictionary if not
intiliaze
if from_node not in self.edges:
self.edges[from_node] = []
if to_node not in self.edges:
self.edges[to_node] = []
self.edges[from_node].append(to_node)
self.edges[to_node].append(from_node)
# Store the distance between from_node and to_node
self.distances[(from_node, to_node)] = distance
self.distances[(to_node, from_node)] = distance
def dijkstra(self, initial):
# Initialize an empty set to store visited nodes
visited = set()
current_distances = {node: float('infinity') for node in self.nodes}
current_distances[initial] = 0
# Loop until all nodes are visited
while len(visited) < len(self.nodes):
# Find the unvisited node with the minimum distance
current_node = None
for node in self.nodes:
if node not in visited and (current_node is None or
current_distances[node] < current_distances[current_node]):
current_node = node
# Mark the current node as visited
visited.add(current_node)
for neighbor in self.edges[current_node]:
distance = current_distances[current_node] +
self.distances[(current_node, neighbor)]
if distance < current_distances[neighbor]:
current_distances[neighbor] = distance
return current_distances
def shortest_path(self, start, end):
distances = self.dijkstra(start)
path = [end]
while end != start:
for neighbor in self.edges[end]:
if distances[end] == distances[neighbor] +
self.distances[(end, neighbor)]:
path.insert(0, neighbor)
end = neighbor
break
return path
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_edge("A", "B", 2)
graph.add_edge("B", "C", 3)
graph.add_edge("C", "D", 5)
graph.add_edge("D", "E", 3)
graph.add_edge("A", "D", 1)
graph.add_edge("C", "E", 2)
graph.add_edge("D", "B", 3)
start_node = "A"
end_node = "E"
shortest_path_result = graph.shortest_path(start_node, end_node)
print(f"Shortest Path from {start_node} to {end_node}:
{shortest_path_result}")
