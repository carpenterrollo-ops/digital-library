"""Flask application routes for managing books and authors."""

import os
from flask import Flask, flash, redirect, render_template, request, url_for
from sqlalchemy import select
from data_models import db, Author, Book
import dbhandler

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{
    os.path.join(
        basedir, 'data/library.sqlite')}"
db.init_app(app)
app.secret_key = 'super_secret_password_for_flash'


@app.route('/add_author', methods=['POST', 'GET'])
def add_author():
    """Handle adding a new author via GET (view form) and POST (submit data)."""
    success_msg = None
    if request.method == 'POST':
        success_msg = "Failed to add author"
        name = request.form.get('name')
        birth_date = request.form.get('birthdate')
        date_of_death = request.form.get('date_of_death')
        dbhandler.add_author(
            Author(
                name=name,
                birth_date=birth_date,
                date_of_death=date_of_death))
        success_msg = f"Successfully added author {name}"

    return render_template("add_author.html", success_message=success_msg)


@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    """Handle adding a new book via GET (view form) and POST (submit data)."""
    success_msg = None
    if request.method == 'POST':
        success_msg = "Failed to add book"
        title = request.form.get('title')
        isbn = request.form.get('isbn')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')
        dbhandler.add_book(
            Book(
                title=title,
                isbn=isbn,
                publication_year=publication_year,
                author_id=author_id))
        success_msg = f"Successfully added book {title}"

    return render_template(
        "add_book.html",
        authors=dbhandler.get_authors(),
        success_message=success_msg
    )

# Statement definieren (1.0 Style)
# @app.route('/', methods=['GET'])
# def index():
#   sort_by = request.args.get('sort_by', 'title')
#
#   query = db.session.query(Book)
#
#   if sort_by == 'author':
#     books = query.join(Author).order_by(Author.name.asc()).all()
#   else:
#     books = query.order_by(Book.title.asc()).all()
#
#   return render_template('home.html', books=books, current_sort=sort_by)
#
#
# @app.route('/search', methods=['GET'])
# def search():
#   search_for = request.args.get('search_for', '')
#
#   stmt = select(Book).where(Book.title.like(f'%{search_for}%'))
#   books = db.session.execute(stmt).scalars().all()
#
#   return render_template('home.html', books=books)


@app.route('/', methods=['GET'])
def home():
    """Display all books with optional search filtering and sorting."""
    # Statement definieren (2.0 Style)
    search_query = request.args.get('search', '').strip()
    sort_by = request.args.get('sort_by', 'title')

    stmt = select(Book)

    if search_query:
        stmt = stmt.where(Book.title.like(f'%{search_query}%'))

    if sort_by == 'author':
        stmt = stmt.join(Author).order_by(Author.name.asc())
    else:
        stmt = stmt.order_by(Book.title.asc())

    books = db.session.execute(stmt).scalars().all()

    return render_template(
        'home.html', books=books, search_query=search_query, current_sort=sort_by
    )


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id: int):
    """Delete a book and remove its author if no associated books remain."""
    book = db.session.get(Book, book_id)

    if not book:
        flash('Das Buch wurde nicht gefunden.', 'danger')
        return redirect(url_for('home'))

    author = book.author
    title = book.title

    db.session.delete(book)
    db.session.commit()

    if author and len(author.books) == 0:
        db.session.delete(author)
        db.session.commit()
        flash(
            f'Buch "{title}" und Autor "{
                author.name}" (keine weiteren Bücher vorhanden) wurden gelöscht! 🗑️',
            'success',
        )
    else:
        flash(f'Buch "{title}" wurde erfolgreich gelöscht! 🗑️', 'success')

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
