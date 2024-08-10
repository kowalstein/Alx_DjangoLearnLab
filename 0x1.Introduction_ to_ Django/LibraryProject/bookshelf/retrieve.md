# Import model
from bookshelf.models import Book

# Retrieve books
books = Book.objects.all()