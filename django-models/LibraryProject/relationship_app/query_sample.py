import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Query all books by a specific author
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}: ")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

def list_books_in_library(library_name):
    """
    List all books in a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in '{library_name}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

def retrieve_librarian_for_libray(library_name):
    """
    Retrieve the librarian for a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        if librarian:
            print(f"Librarian for '{library_name}': {librarian.name}")
        else:
            print(f"No librarian assigned to '{library_name}'.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"Librarian for '{library_name}' does not exist.")


if __name__ == "__main__":
    # Sample queries
    query_books_by_author("Chinua Achebe")
    list_books_in_library("National Library")
    retrieve_librarian_for_libray("Portharcourt Library")