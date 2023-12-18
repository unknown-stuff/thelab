class DivideConquerSort:
def quicksort(self, arr):
if len(arr) <= 1:
return arr
pivot = arr[len(arr) // 2]
left, middle, right = [], [], []
for x in arr:
if x < pivot:
left.append(x)
elif x == pivot:
middle.append(x)
else:
right.append(x)
return self.quicksort(left) + middle + self.quicksort(right)
def display_sorted_data(self, sorted_data):
print("Sorted Data Set:", sorted_data)
data_set = [54, 67, 23, 10, 5, 9, 45, 96, 49]
sort_instance = DivideConquerSort()
print("Original Data Set:", data_set)
sorted_data = sort_instance.quicksort(data_set)
sort_instance.display_sorted_data(sorted_data)
