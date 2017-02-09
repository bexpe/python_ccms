import sqlite3


class Student:
    def get_list_of_students(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()
        mentor_list = []
        for item in self.c.execute("SELECT * FROM Student"):
            mentor_list.append(item)
        print(mentor_list)

    def add_student(self, *args):
        try:
            self.conn.execute("INSERT INTO Student VALUES (NULL,'{}','{}','{}','{}')".format(*args))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def remove_student_from_database(self, student_id):
        try:
            self.c.execute("DELETE FROM Student WHERE id={}".format(student_id))
            self.conn.commit()
        except sqlite3.OperationalError:
            print("Cant remove Table from database")
