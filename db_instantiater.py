"""Module for initializing database tables within the application context."""
from data_models import db
from app import app

with app.app_context():
    db.create_all()
