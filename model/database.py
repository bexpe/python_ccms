import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('database.db')  # connection to database
        self.cursor = self.conn.cursor()

    def close(self):
        """
        Closing the database
        """
        self.conn.close()

    def set(self, command, values=None):
        """
        This method executes a command with value or without if there is no value
        :param command:
        :param values:
        :return: returns the id of last added row to the database
        """
        if values is None:
            self.cursor.execute(command)
        else:
            self.cursor.execute(command, values)
        self.conn.commit()
        return self.cursor.lastrowid  # returns last set to the database row's id

    def get(self, command, values=None):
        """
        This method is taking some data from database
        :param command:
        :param values:
        :return: data got from the database
        """
        if values is None:
            self.cursor.execute(command)
        else:
            self.cursor.execute(command, values)
        data = self.cursor.fetchall()
        return data
