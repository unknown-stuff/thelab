class MaxMinFinder:
    def __init__(self, arr):
        self.arr = arr

    # Function to find the maximum and minimum elements using divide and conquer
    def find_max_min(self, low, high):
        if low == high:  # Only one element in the array
            return (self.arr[low], self.arr[low])

        elif high == low + 1:  # Two elements in the array
            if self.arr[low] > self.arr[high]:
                return (self.arr[low], self.arr[high])
            else:
                return (self.arr[high], self.arr[low])

        else:
            mid = (low + high) // 2
            max1, min1 = self.find_max_min(low, mid)
            max2, min2 = self.find_max_min(mid + 1, high)

            return (max(max1, max2), min(min1, min2))

    # Function to perform binary search on the array
    def binary_search(self, low, high, x):
        try:
            if high >= low:
                mid = low + (high - low) // 2

                if self.arr[mid] == x:
                    return mid

                elif self.arr[mid] > x:
                    return self.binary_search(low, mid - 1, x)

                else:
                    return self.binary_search(mid + 1, high, x)

            else:
                return -1
        except Exception as e:
            print(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    max_min_finder = MaxMinFinder(arr)
    maximum, minimum = max_min_finder.find_max_min(0, len(arr) - 1)

    print(f"Given array: {arr}")
    print(f"Maximum element is: {maximum}")
    print(f"Minimum element is: {minimum}")

    x = 5
    try:
        result = max_min_finder.binary_search(0, len(arr) - 1, x)
        if result != -1:
            print(f"Element {x} is present at index {result}.")
        else:
            print(f"Element {x} is not present in the array.")
    except Exception as e:
        print(f"An error occurred: {e}")
