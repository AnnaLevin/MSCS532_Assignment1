# Simple Heapsort implementation in Python

def heapify(arr, n, i):
    largest = i          # Assume current node is largest
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Step 1: Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # Move max to the end
        heapify(arr, i, 0)

# Example:
numbers = [12, 11, 13, 5, 6, 7]
print("Original array:", numbers)
heapsort(numbers)
print("Sorted array:", numbers)
