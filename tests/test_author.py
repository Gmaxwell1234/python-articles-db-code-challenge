import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.db.connection import get_connection

def setup_function():
    with get_connection() as conn:
        conn.execute("DELETE FROM authors")

def test_author_save_and_get_all():
    author = Author("Jane Doe")
    author.save()
    authors = Author.get_all()
    assert len(authors) == 1
    assert authors[0].name == "Jane Doe"
