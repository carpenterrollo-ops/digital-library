from data_models import db, Author, Book
from app import app

with app.app_context():
  db.create_all()