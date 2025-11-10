from books_dict import add_book, search_by_isbn
from bst_titles import insert, search, Node
from waitlist_queue import add_to_waitlist, next_in_line

# Create sample data
add_book('001', 'The Odyssey', 'Homer')
add_book('002', 'Pride and Prejudice', 'Jane Austen')

# Build BST
root = None
root = insert(root, 'The Odyssey', '001')
root = insert(root, 'Pride and Prejudice', '002')

# Test searching
print(search_by_isbn('001'))
print(search(root, 'The Odyssey').title)

# Waiting list demo
add_to_waitlist('Anna')
add_to_waitlist('John')
print(next_in_line())  # Anna
