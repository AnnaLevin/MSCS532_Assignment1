# bst_titles.py
class Node:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.left = None
        self.right = None

def insert(root, title, isbn):
    if not root:
        return Node(title, isbn)
    if title < root.title:
        root.left = insert(root.left, title, isbn)
    else:
        root.right = insert(root.right, title, isbn)
    return root

def search(root, title):
    if not root:
        return None
    if title == root.title:
        return root
    elif title < root.title:
        return search(root.left, title)
    else:
        return search(root.right, title)
