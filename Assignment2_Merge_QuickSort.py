import time, random

# ---------- Merge Sort ----------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------- Quick Sort ----------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# ---------- Performance Test ----------
data_random = [random.randint(0, 10000) for _ in range(1000)]

start = time.time()
merge_sort(data_random.copy())
print("Merge Sort time:", round(time.time() - start, 5), "sec")

start = time.time()
quick_sort(data_random.copy())
print("Quick Sort time:", round(time.time() - start, 5), "sec")

# Test with already sorted data
data_sorted = sorted(data_random)
# Test with reverse sorted data
data_reverse = sorted(data_random, reverse=True)

for dataset_name, dataset in [
    ("Random", data_random),
    ("Sorted", data_sorted),
    ("Reverse Sorted", data_reverse)
]:
    start = time.time()
    merge_sort(dataset.copy())
    merge_time = time.time() - start

    start = time.time()
    quick_sort(dataset.copy())
    quick_time = time.time() - start

    print(f"{dataset_name} Data → Merge: {merge_time:.5f}s | Quick: {quick_time:.5f}s")

