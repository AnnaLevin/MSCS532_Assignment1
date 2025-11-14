import random

# ---------------------------------------------------------
# Deterministic Quicksort (pivot = last element)
# ---------------------------------------------------------
def quicksort(arr):
    # Base case: list with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]          # Fixed pivot choice (last element)
    left = []                # Elements <= pivot
    right = []               # Elements > pivot

    # Partition step
    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    # Recursively sort left and right sides
    return quicksort(left) + [pivot] + quicksort(right)


# ---------------------------------------------------------
# Randomized Quicksort (pivot = random element)
# ---------------------------------------------------------
def randomized_quicksort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)   # Random pivot
    left = []
    equal = []
    right = []

    # Partition step using the random pivot
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)

    # Recursively sort sublists and combine results
    return randomized_quicksort(left) + equal + randomized_quicksort(right)


# ---------------------------------------------------------
# Example usage (this part runs when file is executed)
# ---------------------------------------------------------
if __name__ == "__main__":
    data = [8, 3, 1, 7, 0, 10, 2]

    print("Original list:", data)
    print("Deterministic Quicksort:", quicksort(data))
    print("Randomized Quicksort:", randomized_quicksort(data))
