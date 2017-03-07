import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def set(self, command, values=None):
        self.cursor.execute(command, values)
        self.conn.commit()

    def get(self, command, values=(0,)):
        self.cursor.execute(command, values)
        data = self.cursor.fetchall()
        return data

# db = Database()
# db.command("sdasdasd")
# db.close_database()
# db.get("select ")