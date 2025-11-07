import heapq

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        # Lower number = higher priority
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

# Example usage:
pq = PriorityQueue()
pq.insert(Task("Do homework", 2))
pq.insert(Task("Wash dishes", 3))
pq.insert(Task("Pay bills", 1))

print("\nTasks in order of priority:")
while not pq.is_empty():
    task = pq.extract_min()
    print(task)
