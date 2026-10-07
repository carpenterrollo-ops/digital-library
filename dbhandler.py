"""Database helper functions for adding and querying authors and books."""
from data_models import db, Author, Book


def add_author(author: Author):
    """Add a new Author instance to the database."""
    db.session.add(author)
    db.session.commit()


def add_book(book: Book):
    """Add a new Book instance to the database."""
    db.session.add(book)
    db.session.commit()


def get_authors():
    """Retrieve all authors from the database."""
    return db.session.query(Author).all()


def get_books():
    """Retrieve all books from the database."""
    return db.session.query(Book).all()
