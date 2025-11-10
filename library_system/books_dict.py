# books_dict.py
# will store and manage books (dictionary)

# books_dict.py
books = {}

def add_book(isbn, title, author):
    books[isbn] = {'title': title, 'author': author, 'available': True}

def search_by_isbn(isbn):
    return books.get(isbn, "Book not found")
