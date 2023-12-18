class Kruskal_algorithm:
def __init__(self, nodes, edges):
# Initialize the class with nodes and edges
self.nodes = nodes
self.edges = edges
def find(self, node, parent):
# Find the root of the set to which the node belongs
if parent[node] != node:
parent[node] = self.find(parent[node], parent)
return parent[node]
def union(self, set1, set2, parent, rank):
# Union operation to merge two sets
root1, root2 = self.find(set1, parent), self.find(set2, parent)
if root1 != root2:
if rank[root1] < rank[root2]:
parent[root1] = root2
elif rank[root1] > rank[root2]:
parent[root2] = root1
else:
parent[root1] = root2
rank[root2] += 1
def kruskal(self):
min_spanning_tree = []
# Sorting edges based on weights
self.edges.sort()
parent = {node: node for node in self.nodes}
rank = {node: 0 for node in self.nodes}
for edge in self.edges:
weight, node1, node2 = edge
if self.find(node1, parent) != self.find(node2, parent):
# Add edge to the min_spanning_tree
min_spanning_tree.append((node1, node2, weight))
# Union the sets of node1 and node2
self.union(node1, node2, parent, rank)
return min_spanning_tree
# Example Usage
nodes = {"A", "B", "C", "D"}
edges = [(1, "A", "B"), (3, "A", "C"), (4, "B", "C"), (2, "C", "D"),(2, "D",
"A")]
kruskal_instance = Kruskal_algorithm(nodes, edges)
minimum_spanning_tree = kruskal_instance.kruskal()
print("Minimum Cost Spanning Tree (Kruskal's Algorithm):",
minimum_spanning_tree)
