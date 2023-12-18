import java.util.Arrays;
class Knapsack {
// A utility function that returns maximum of two integers
static int max(int a, int b) {
return (a > b) ? a : b;
}
// Returns the maximum value that can be put in a knapsack of capacity W
static int knapSack(int W, int wt[], int val[], int n) {
int i, w;
int[][] K = new int[n + 1][W + 1];
// Build table K[][] in bottom-up manner
for (i = 0; i <= n; i++) {
for (w = 0; w <= W; w++) {
if (i == 0 || w == 0)
K[i][w] = 0;
else if (wt[i - 1] <= w)
K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i -
1][w]);
else
K[i][w] = K[i - 1][w];
}
}
// Print the table
System.out.println("Dynamic Programming Table:");
for (i = 0; i <= n; i++) {
for (w = 0; w <= W; w++) {
System.out.print(K[i][w] + "\t");
}
System.out.println();
}
// Find the items included in the knapsack
int res = K[n][W];
w = W;
System.out.print("Items included in the knapsack: ");
for (i = n; i > 0 && res > 0; i--) {
if (res == K[i - 1][w])
continue;
else {
System.out.print(wt[i - 1] + " ");
res = res - val[i - 1];
w = w - wt[i - 1];
}
}
return K[n][W];
}
// Driver code
public static void main(String args[]) {
try {
int val[] = {60, 100, 120};
int wt[] = {10, 20, 30};
int W = 50;
int n = val.length;
System.out.println("Maximum value that can be obtained is " + 
knapSack(W, wt, val, n));
} catch (Exception e) {
System.out.println("An error occurred: " + e.getMessage());
e.printStackTrace();
}
}
}
