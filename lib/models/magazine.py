from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", (self.name, self.category, self.id))
        conn.commit()

    @classmethod
    def get_all(cls):
        cursor = get_connection().cursor()
        rows = cursor.execute("SELECT id, name, category FROM magazines").fetchall()
        return [cls(name=row[1], category=row[2], id=row[0]) for row in rows]
