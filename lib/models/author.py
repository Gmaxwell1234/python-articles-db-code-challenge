from lib.db.connection import get_connection

class Author:
    """Represents an author who writes articles for magazines."""

    def __init__(self, name, id=None):
        """
        Initialize an Author instance.

        Args:
            name (str): The name of the author.
            id (int, optional): The unique ID of the author. Defaults to None.
        """
        self.id = id
        self.name = name

    def save(self):
        """
        Save the Author to the database.

        If the author doesn't have an ID, a new record is inserted.
        If the author has an ID, the existing record is updated.
        """
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id))
        conn.commit()

    @classmethod
    def get_all(cls):
        """
        Retrieve all authors from the database.

        Returns:
            list[Author]: A list of Author instances.
        """
        cursor = get_connection().cursor()
        rows = cursor.execute("SELECT id, name FROM authors").fetchall()
        return [cls(name=row[1], id=row[0]) for row in rows]
