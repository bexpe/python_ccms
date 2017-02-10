import sqlite3


class StudentModel:

    def __init__(self):
        self.conn = sqlite3.connect('baza_danych.db')
        self.c = self.conn.cursor()

    def get_list_of_students(self):
        student_list = []
        for item in self.c.execute("SELECT * FROM Student"):
            student_list.append(item)
        return student_list

    def add_student(self, *args):
        try:
            self.c.execute("INSERT INTO Student(name, surname, email, date_of_birth, city, phone) VALUES ('{}','{}','{}','{}','{}','{}')".format(*args))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def remove_student_from_database(self, name_student, surname_student):
        try:
            self.c.execute("DELETE FROM Student WHERE name='{}' and surname='{}'".format(name_student, surname_student))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant remove Table from database {}".format(w))

    def get_student_detail(self, name, surname):
        student_detail = []
        try:
            get_student = self.c.execute("SELECT name, surname, email, date_of_birth, city, phone, attendance_level, card FROM Student"
                                         " WHERE name = '{}' and surname = '{}'".format(name, surname))
            for item in get_student:
                student_detail.append(item)
            self.conn.commit()
            return student_detail
        except sqlite3.OperationalError as w:
            print("Cant get student {}".format(w))

    def edit_student(self, cur_name, cur_surname, *args):
        try:
            self.c.execute("UPDATE Student SET Name = '{}', Surname = '{}',Email = '{}', Date_of_birth = '{}',"
                           "City = '{}', Phone = '{}' WHERE name = '{}' and surname = '{}'".format(*args, cur_name, cur_surname))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant edit mentor: {}".format(w))

    def add_card(self, cards, name, surname):
        try:
            self.c.execute("UPDATE Student SET Card = '{}' WHERE name = '{}' and surname = '{}'".format(cards, name, surname))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add card {}".format(w))

    @staticmethod
    def db_get_attendance_by_id(student_id):
        """
        Get attendance list by student id.
        :param student_id:
        :return: attendance_list_by_student
        """
        connect = sqlite3.connect('data/data.db')
        cur = connect.cursor()
        cur.execute("SELECT Attendance_value, Date FROM Student_Attendance WHERE Student_id = (?)", student_id)
        connect.commit()

        attendance_list_by_student = cur.fetchall()
        return attendance_list_by_student

    def close_database(self):
        self.conn.close()


