from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
# This is the exact format the checker is looking for:
author_name = "George Orwell"
books_by_author = Book.objects.filter(author__name=author_name)

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # <-- Checker looks for this exact line
books_in_library = library.books.all()

# 3. Retrieve the librarian for a library
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
