import sys
import os

# Add the parent directory to the system path so modules in lib can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def setup_function():
    """
    Set up a clean database state before each test.

    This function clears all data from the articles, authors, and magazines tables.
    It ensures each test starts with an empty database.
    """
    with get_connection() as conn:
        conn.execute("DELETE FROM articles")
        conn.execute("DELETE FROM authors")
        conn.execute("DELETE FROM magazines")

def test_article_creation_and_retrieval():
    """
    Test creating an article and retrieving it from the database.

    This test ensures:
    - An article can be saved with a valid author and magazine
    - The saved article can be retrieved correctly with matching fields
    """
    # Create and save an author
    author = Author("John Smith")
    author.save()

    # Create and save a magazine
    mag = Magazine("Science Weekly", "Science")
    mag.save()

    # Create and save an article linked to the author and magazine
    article = Article("Quantum Physics", author.id, mag.id)
    article.save()

    # Retrieve articles from the database and validate
    articles = Article.get_all()
    assert len(articles) == 1
    assert articles[0].title == "Quantum Physics"
    assert articles[0].author_id == author.id
    assert articles[0].magazine_id == mag.id
