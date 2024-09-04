## Testing Documentation

### Test Cases

- **Create Book:** Verifies that a new book is created and returned correctly.
- **Read Book:** Ensures that the details of a book can be retrieved.
- **Update Book:** Confirms that updates to a book are reflected in the database.
- **Delete Book:** Checks that a book can be deleted from the database.
- **Filter Books:** Tests filtering functionality to return the correct subset of books.
- **Search Books:** Verifies that search functionality works correctly.
- **Order Books:** Ensures that ordering functionality sorts books as expected.
- **Unauthorized Access:** Tests that unauthorized users cannot access protected endpoints.

### Running Tests

Run the tests using:
```bash
python manage.py test api
