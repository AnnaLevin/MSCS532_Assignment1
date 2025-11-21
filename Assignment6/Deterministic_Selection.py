def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: split into groups of 5
    chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]

    # Step 2: find pivot using recursion
    pivot = median_of_medians(medians, len(medians)//2)

    # Step 3: partition around pivot
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))


# Example:
arr = [7, 3, 10, 4, 6, 2]
print("Deterministic:", median_of_medians(arr, 2))
