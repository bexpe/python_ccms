import sqlite3


class Student:
    def get_list_of_students(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()
        student_list = []
        for item in self.c.execute("SELECT * FROM Student"):
            student_list.append(item)
        print(student_list)

    def add_student(self, *args):
        try:
            self.conn.execute("INSERT INTO Student VALUES (NULL,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')". \
                              format(*args))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def remove_student_from_database(self, student_id):
        try:
            self.c.execute("DELETE FROM Student WHERE id={}".format(student_id))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant remove Table from database {}".format(w))

    def get_student_detali(self, name, surname):
        student_detail = []
        try:
            get_student = self.c.execute("SELECT name, surname, email, city, phone FROM Student"
                                         " WHERE name = {} and surname = {}".format(name, surname))
            for item in get_student:
                student_detail.append(item)
            self.conn.commit()
            return student_detail
        except sqlite3.OperationalError as w:
            print("Cant get student {}".format(w))


s = Student()
s.get_list_of_students()

s.get_student_detali("1","1")
print(s.get_student_detali("1","1"))

