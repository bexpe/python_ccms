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

    def get_student_detail(self, name, surname, student_list):
        student_detail = []
        try:
            get_student = self.c.execute("SELECT name, surname, email, date_of_birth, city, phone, attendance_level, card FROM Student"
                                         " WHERE name = '{}' and surname = '{}'".format(name, surname))
            for student in student_list:
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

    def check_student_in_db_by_id_model(self, student_id):
        """
        Check if student exists in database.
        :param student_id:
        :return: boolean
        """
        try:
            self.c.execute("SELECT ID FROM Student WHERE ID = {}".format(student_id))
            self.conn.commit()
            return True
        except sqlite3.OperationalError as w:
            print("Can't check if student exists {}".format(w))

    def close_database(self):
        self.conn.close()


