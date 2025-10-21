# insertion_sort_descending.py

def insertion_sort_descending(arr):
    """
    Sorts an array in monotonically decreasing order using the Insertion Sort algorithm.
    Based on Introduction to Algorithms (Cormen et al., 2022), Chapter 2.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:  # Compare and shift smaller elements to the right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

