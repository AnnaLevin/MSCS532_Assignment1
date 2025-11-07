# Assignment 4: Heap Data Structures – Implementation, Analysis, and Applications

## 📘 Course Information
**Course:** Algorithms and Data Structures (MSCS-532-B01)  
**Student:** Anna Levinskaia  
**University:** University of the Cumberlands  
**Date:** November 2025  

---

## 🧩 Overview
This project demonstrates how **heap data structures** work and how they can be applied to:
- **Heapsort** (sorting using a max-heap)
- **Priority Queue** (task scheduling using a min-heap)

Both implementations are written in **Python** using lists to represent heaps.

---

## ⚙️ Heapsort Implementation

**File:** `heapsort.py`

### Description
The program builds a **max-heap** and then sorts the array in ascending order by repeatedly moving the largest element to the end.

### Example Code
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

numbers = [12, 11, 13, 5, 6, 7]
print("Original array:", numbers)
heapsort(numbers)
print("Sorted array:", numbers)
```

### Example Output
```
Original array: [12, 11, 13, 5, 6, 7]
Sorted array: [5, 6, 7, 11, 12, 13]
```

### Complexity
| Case | Time Complexity | Space |
|------|------------------|--------|
| Best | O(n log n) | O(1) |
| Average | O(n log n) | O(1) |
| Worst | O(n log n) | O(1) |

Heapsort works consistently in **O(n log n)** for all input types and sorts **in place**, without extra memory.

---

## 🧮 Priority Queue Implementation

**File:** `priority_queue.py`

### Description
Implements a **Priority Queue** using Python’s built-in `heapq` module, which is based on a **min-heap**.  
Smaller priority values represent higher importance.

### Example Code
```python
import heapq

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"{self.name} (priority: {self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        heapq.heappush(self.heap, task)
        print(f"Inserted: {task}")

    def extract_min(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
```

### Example Output
```
Inserted: Do homework (priority: 2)
Inserted: Wash dishes (priority: 3)
Inserted: Pay bills (priority: 1)

Tasks in order of priority:
Pay bills (priority: 1)
Do homework (priority: 2)
Wash dishes (priority: 3)
```

### Complexity
| Operation | Description | Time |
|------------|--------------|------|
| `insert()` | Add a new task | O(log n) |
| `extract_min()` | Remove the highest-priority task | O(log n) |
| `is_empty()` | Check if the queue is empty | O(1) |

All operations are efficient and ideal for **real-world scheduling**, such as CPU task management or print queue handling.

---

## 🧠 Summary of Findings
- **Heapsort** runs in **O(n log n)** time in all cases and sorts **in place**.  
- **Priority Queue** supports quick insertions and removals with **O(log n)** performance.  
- Heaps are extremely useful in real systems like **task scheduling**, **event simulation**, and **data prioritization**.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heap-assignment.git
   cd heap-assignment
   ```

2. Run Heapsort:
   ```bash
   python heapsort.py
   ```

3. Run Priority Queue:
   ```bash
   python priority_queue.py
   ```

---

## 👩‍💻 Author
**Anna Levinskaia**  
Algorithms and Data Structures (MSCS-532-B01)  
University of the Cumberlands  

---

## 📝 License
This project is for academic and educational purposes.
