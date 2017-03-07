import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def set(self, command):
        self.cursor.execute(command)
        self.conn.commit()

    def get(self, command):
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return data

# db = Database()
# db.command("sdasdasd")
# db.close_database()
# db.get("select ")