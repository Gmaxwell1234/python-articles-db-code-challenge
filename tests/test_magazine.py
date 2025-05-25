# Add the parent directory to sys.path to allow imports from lib package
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary modules
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def setup_function():
    """
    Resets the magazines table before each test by deleting all rows.
    This ensures a clean test environment.
    """
    with get_connection() as conn:
        conn.execute("DELETE FROM magazines")

def test_magazine_save_and_get_all():
    """
    Tests the save and get_all methods for the Magazine class.

    1. Creates a new magazine instance and saves it to the database.
    2. Fetches all magazines from the database.
    3. Asserts that only one magazine exists and that its fields are correct.
    """
    mag = Magazine("Tech Monthly", "Tech")
    mag.save()
    mags = Magazine.get_all()

    assert len(mags) == 1               # Ensure only one magazine was saved
    assert mags[0].name == "Tech Monthly"
    assert mags[0].category == "Tech"
