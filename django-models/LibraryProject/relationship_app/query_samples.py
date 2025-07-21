from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (e.g., 'George Orwell')
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)

# 2. List all books in a library (e.g., 'City Library')
library = Library.objects.get(name="City Library")
books_in_library = library.books.all()

# 3. Retrieve the librarian for a library (e.g., 'City Library')
librarian = Librarian.objects.get(library=library)
