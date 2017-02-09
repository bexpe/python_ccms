import sqlite3


class Employee:

    def __init__(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()

    def get_list_of_employees(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()
        mentor_list = []
        for item in self.c.execute("SELECT * FROM Employee"):
            mentor_list.append(item)
        print(mentor_list)

    def add_mentor(self, *args):
        try:
            self.conn.execute("INSERT INTO Employee VALUES (NULL,'{}','{}','{}','{}')".format(*args))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def remove_mentor_from_database(self, employee_id):
        try:
            self.c.execute("DELETE FROM Employee WHERE id={}".format(employee_id))
            self.conn.commit()
        except sqlite3.OperationalError:
            print("Cant remove Table from database")

    def close_database(self):
        self.conn.close()
