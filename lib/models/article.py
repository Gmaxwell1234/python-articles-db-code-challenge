from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (self.title, self.author_id, self.magazine_id)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                (self.title, self.author_id, self.magazine_id, self.id)
            )
        conn.commit()

    @classmethod
    def get_all(cls):
        cursor = get_connection().cursor()
        rows = cursor.execute("SELECT id, title, author_id, magazine_id FROM articles").fetchall()
        return [cls(title=row[1], author_id=row[2], magazine_id=row[3], id=row[0]) for row in rows]
