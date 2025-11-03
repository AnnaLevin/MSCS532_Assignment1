import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)       # choose pivot randomly
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

def deterministic_quicksort_first(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]                   # first element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quicksort_first(left) + middle + deterministic_quicksort_first(right)

# Example test
data = [5, 3, 8, 3, 9, 1, 5, 2, 7, 6]

print("Original:", data)
print("Randomized Quicksort:", randomized_quicksort(data))
print("Deterministic Quicksort:", deterministic_quicksort_first(data))
