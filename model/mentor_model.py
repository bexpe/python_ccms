import sqlite3


class Mentor:

    def __init__(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()

    def get_list_of_mentors(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()
        mentor_list = []
        for item in self.c.execute("SELECT * FROM Mentor"):
            mentor_list.append(item)
        print(mentor_list)

    def add_mentor(self, *args):
        try:
            self.conn.execute("INSERT INTO Mentor VALUES (NULL,'{}','{}','{}','{}','{}','{}','{}','{}')".format(*args))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def remove_mentor_from_database(self, mentor_id):
        try:
            self.c.execute("DELETE FROM Mentor WHERE id={}".format(mentor_id))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant remove Table from database: {}".format(w))

    def close_database(self):
        self.conn.close()

    def edit_mentor(self, mentor_id, *args):
        try:
            self.c.execute("UPDATE Mentor SET Name = '{}', Surname = '{}',Email = '{}',"
                           "City = '{}', Phone = '{}' WHERE ID = {}".format(*args, mentor_id))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant edit mentor: {}".format(w))

    def get_mentor_detail(self, name, surname):
        mentor_detail = []
        try:
            get_student = self.c.execute("SELECT name, surname, email, city, phone FROM Mentor"
                                         " WHERE name = {} and surname = {}".format(name, surname))
            for item in get_student:
                mentor_detail.append(item)
            self.conn.commit()
            return mentor_detail
        except sqlite3.OperationalError as w:
            print("Cant get student {}".format(w))

c = Mentor()

c.get_list_of_mentors()
c.edit_mentor(1, "123312", "33", "", "", "zzz")
c.edit_mentor(2, "1", "2", "", "", "zzz")
c.get_list_of_mentors()
print(c.get_mentor_detail("1", "2"))