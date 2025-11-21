import time
import random
from books_dict import add_book, search_by_isbn
from bst_titles import insert, search, build_balanced_bst
from waitlist_queue import add_to_waitlist, next_in_line

print("=== Phase 3 Performance Testing ===")

# 1. Generate large dataset
N = 10000
titles = [f"Book Title {i}" for i in range(N)]
books_data = [(titles[i], f"{1000+i}") for i in range(N)]

# 2. Measure dictionary performance
print("\nTesting dictionary insertion...")
start = time.time()
for title, isbn in books_data:
    add_book(isbn, title, f"Author {isbn}")
end = time.time()
print(f"Insertion time for {N} books: {round(end-start, 3)} s")

# 3. Build a balanced BST
print("\nBuilding balanced BST...")
root = build_balanced_bst(books_data)

# 4. Search performance
print("\nTesting search performance...")
sample_titles = random.sample(titles, 1000)
start = time.time()
for t in sample_titles:
    search(root, t)
end = time.time()
print(f"Search time for 1,000 titles: {round(end-start, 3)} s")

# 5. Queue test
print("\nTesting queue operations...")
start = time.time()
for i in range(1000):
    add_to_waitlist(f"User{i}")
for i in range(1000):
    next_in_line()
end = time.time()
print(f"Queue operations time: {round(end-start, 4)} s")

print("\n=== Testing Complete ===")
