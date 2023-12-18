import java.util.Scanner;
import java.util.Arrays;
public class UniqueSortingApp {
private static void customQuickSort(int[] arr, int low, int high) {
if (low < high) {
int partitionIndex = customPartition(arr, low, high);
customQuickSort(arr, low, partitionIndex - 1);
customQuickSort(arr, partitionIndex + 1, high);
}
}
private static int customPartition(int[] arr, int low, int high) {
int pivot = arr[high];
int i = (low - 1);
for (int j = low; j < high; j++) {
if (arr[j] < pivot) {
i++;
int temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
}
}
int temp = arr[i + 1];
arr[i + 1] = arr[high];
arr[high] = temp;
return i + 1;
}
private static void customMergeSort(int[] arr) {
if (arr == null || arr.length <= 1) {
return;
}
int mid = arr.length / 2;
int[] left = Arrays.copyOfRange(arr, 0, mid);
int[] right = Arrays.copyOfRange(arr, mid, arr.length);
customMergeSort(left);
customMergeSort(right);
customMerge(arr, left, right);
}
private static void customMerge(int[] arr, int[] left, int[] right) {
int i = 0, j = 0, k = 0;
while (i < left.length && j < right.length) {
if (left[i] < right[j]) {
arr[k++] = left[i++];
} else {
arr[k++] = right[j++];
}
}
while (i < left.length) {
arr[k++] = left[i++];
}
while (j < right.length) {
arr[k++] = right[j++];
}
}
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
try {
System.out.println("Enter the number of elements: ");
int n = scanner.nextInt();
int[] data = new int[n];
System.out.println("Enter the elements:");
for (int i = 0; i < n; i++) {
data[i] = scanner.nextInt();
}
System.out.println("Choose a sorting algorithm (1 for Quick Sort, 
2 for Merge Sort): ");
int choice = scanner.nextInt();
if (choice == 1) {
customQuickSort(data, 0, n - 1);
System.out.println("Sorted array using Quick Sort:");
} else if (choice == 2) {
customMergeSort(data);
System.out.println("Sorted array using Merge Sort:");
} else {
System.out.println("Invalid choice.");
return;
}
for (int value : data) {
System.out.print(value + " ");
}
} catch (Exception e) {
System.out.println("An error occurred: " + e.getMessage());
} finally {
// Closing the scanner in the finally block
if (scanner != null) {
scanner.close();
}
}
}
}
