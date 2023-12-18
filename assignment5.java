class ShortestPathDijkstra {
private static final int V = 9;
// Utility function to find the vertex with the minimum distance value
private int minDistance(int[] dist, Boolean[] sptSet) {
int min = Integer.MAX_VALUE;
int min_index = -1;
for (int v = 0; v < V; v++) {
if (!sptSet[v] && dist[v] <= min) {
min = dist[v];
min_index = v;
}
}
return min_index;
}
// Utility function to print the constructed distance array
private void printSolution(int[] dist, int n) {
System.out.println("Vertex \t\t Distance from Source");
for (int i = 0; i < V; i++)
System.out.println(i + " \t\t " + dist[i]);
}
// Function that implements Dijkstra's single source shortest path 
algorithm for a graph represented using adjacency matrix
private void dijkstra(int[][] graph, int src) {
int[] dist = new int[V]; // The output array dist[i] will hold the 
shortest distance from src to i
// sptSet[i] will be true if vertex i is included in the shortest path 
tree or the shortest distance from src to i is finalized
Boolean[] sptSet = new Boolean[V];
// Initialize all distances as INFINITE and sptSet[] as false
for (int i = 0; i < V; i++) {
dist[i] = Integer.MAX_VALUE;
sptSet[i] = false;
}
// Distance of source vertex from itself is always 0
dist[src] = 0;
// Find shortest path for all vertices
for (int count = 0; count < V - 1; count++) {
int u = minDistance(dist, sptSet);
sptSet[u] = true;
// Update dist value of the adjacent vertices of the picked 
vertex.
for (int v = 0; v < V; v++)
if (!sptSet[v] && graph[u][v] != 0 && dist[u] != 
Integer.MAX_VALUE && dist[u] + graph[u][v] < dist[v])
dist[v] = dist[u] + graph[u][v];
}
// Print the constructed distance array
printSolution(dist, V);
}
public static void main(String[] args) {
try {
ShortestPathDijkstra t = new ShortestPathDijkstra();
int[][] graph = { { 0, 4, 0, 0, 0, 0, 0, 8, 0 },
{ 4, 0, 8, 0, 0, 0, 0, 11, 0 },
{ 0, 8, 0, 7, 0, 4, 0, 0, 2 },
{ 0, 0, 7, 0, 9, 14, 0, 0, 0 },
{ 0, 0, 0, 9, 0, 10, 0, 0, 0 },
{ 0, 0, 4, 14, 10, 0, 2, 0, 0 },
{ 0, 0, 0, 0, 0, 2, 0, 1, 6 },
{ 8, 11, 0, 0, 0, 0, 1, 0, 7 },
{ 0, 0, 2, 0, 0, 0, 6, 7, 0 } };
t.dijkstra(graph, 0);
} catch (Exception e) {
System.out.println("An error occurred: " + e.getMessage());
}
}
}
