from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
import json

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    author_id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    birth_date: Mapped[str]
    date_of_death: Mapped[str|None]

    # Optional: Ermöglicht Zugriff auf alle Bücher eines Autors via author.books
    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")

    def __repr__(self):
        return json.dumps({
            "author_id": self.author_id,
            "name": self.name,
            "birth_date": self.birth_date,
            "date_of_death": self.date_of_death
        }, indent=1)

    def __str__(self) -> str:
        return f"name: {self.name} birth date: {self.birth_date} death date: {self.date_of_death}"

class Book(db.Model):
    __tablename__ = 'books'
    book_id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('authors.author_id'))
    isbn: Mapped[str]
    publication_year: Mapped[str]
    # Hier wird die Beziehung definiert:
    author: Mapped["Author"] = relationship("Author", back_populates="books")

    def __repr__(self):
        return json.dumps({"book_id": self.book_id, "title": self.title, "author_id": self.author_id}, indent=1)

    def __str__(self) -> str:
        return f"title: {self.title} isbn: {self.isbn} publication_year: {self.publication_year}"

