"""Script to seed the database with sample authors and books via HTTP POST requests."""

import requests

BASE_URL = "http://127.0.0.1:5000"

authors_data = [
    {
        "name": "J.K. Rowling",
        "birthdate": "1965-07-31",
        "date_of_death": "",
    },
    {
        "name": "George Orwell",
        "birthdate": "1903-06-25",
        "date_of_death": "1950-01-21",
    },
    {
        "name": "J.R.R. Tolkien",
        "birthdate": "1892-01-03",
        "date_of_death": "1973-09-02",
    },
    {
        "name": "Stephen King",
        "birthdate": "1947-09-21",
        "date_of_death": "",
    },
    {
        "name": "Agatha Christie",
        "birthdate": "1890-09-15",
        "date_of_death": "1976-01-12",
    },
    {
        "name": "Frank Herbert",
        "birthdate": "1920-10-08",
        "date_of_death": "1986-02-11",
    },
    {
        "name": "Franz Kafka",
        "birthdate": "1883-07-03",
        "date_of_death": "1924-06-03",
    },
    {
        "name": "Harper Lee",
        "birthdate": "1926-04-28",
        "date_of_death": "2016-02-19",
    },
    # Neu hinzugefügt: Terry Pratchett
    {
        "name": "Terry Pratchett",
        "birthdate": "1948-04-28",
        "date_of_death": "2015-03-12",
    },
]

# Bücher (author_id entspricht der Reihenfolge beim Anlegen)
books_data = [
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "publication_year": "1997",
        "isbn": "9780747532699",
        "author_id": 1,
    },
    {
        "title": "1984",
        "publication_year": "1949",
        "isbn": "9780451524935",
        "author_id": 2,
    },
    {
        "title": "The Hobbit",
        "publication_year": "1937",
        "isbn": "9780261102217",
        "author_id": 3,
    },
    {
        "title": "The Shining",
        "publication_year": "1977",
        "isbn": "9780307743657",
        "author_id": 4,
    },
    {
        "title": "Murder on the Orient Express",
        "publication_year": "1934",
        "isbn": "9780007119318",
        "author_id": 5,
    },
    {
        "title": "Dune",
        "publication_year": "1965",
        "isbn": "9780441172719",
        "author_id": 6,
    },
    {
        "title": "Die Verwandlung",
        "publication_year": "1915",
        "isbn": "9783150099001",
        "author_id": 7,
    },
    {
        "title": "To Kill a Mockingbird",
        "publication_year": "1960",
        "isbn": "9780061120084",
        "author_id": 8,
    },
    {
        "title": "The Colour of Magic",
        "publication_year": "1983",
        "isbn": "9780540058860",
        "author_id": 9,
    },
    {
        "title": "Guards! Guards!",
        "publication_year": "1989",
        "isbn": "9780552134620",
        "author_id": 9,
    },
    {
        "title": "Mort",
        "publication_year": "1987",
        "isbn": "9780552131063",
        "author_id": 9,
    },
]


def seed_database():
    """Send requests to backend API endpoints to populate database."""
    print("--- Füge Autoren hinzu ---")
    for author in authors_data:
        response = requests.post(
            f"{BASE_URL}/add_author",
            data=author,
            timeout=10)
        if response.status_code in (200, 201):
            print(f"✅ Autor hinzugefügt: {author['name']}")
        else:
            print(
                f"❌ Fehler bei Autor {
                    author['name']}: Status {
                    response.status_code}"
            )

    print("\n--- Füge Bücher hinzu ---")
    for book in books_data:
        response = requests.post(f"{BASE_URL}/add_book", data=book, timeout=10)
        if response.status_code in (200, 201):
            print(f"✅ Buch hinzugefügt: {book['title']}")
        else:
            print(
                f"❌ Fehler bei Buch {
                    book['title']}: Status {
                    response.status_code}"
            )


if __name__ == "__main__":
    seed_database()
