from data_models import db, Author, Book

def add_author(author: Author):
    db.session.add(author)
    db.session.commit()

def add_book(book: Book):
    db.session.add(book)
    db.session.commit()

def get_authors():
    return db.session.query(Author).all()

def get_books():
    return db.session.query(Book).all()