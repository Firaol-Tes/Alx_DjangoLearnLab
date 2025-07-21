# delete.md

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by trying to retrieve all books
Book.objects.all()

# Expected Output:
# <QuerySet []>
