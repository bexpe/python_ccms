import sqlite3


class Mentor_model:

    def __init__(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()

    def get_list_of_mentors(self):
        mentor_list = []git
        for item in self.c.execute("SELECT * FROM Mentor"):
            mentor_list.append(item)
        return mentor_list

    def add_mentor(self, *args):
        #TODO
        #patrz kontroler co dostajesz
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
        #TODO
        #spójrz na kontroler
        try:
            self.c.execute("UPDATE Mentor SET Name = '{}', Surname = '{}',Email = '{}',"
                           "City = '{}', Phone = '{}' WHERE ID = {}".format(*args, mentor_id))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant edit mentor: {}".format(w))

    def get_mentor_detail(self, name, surname):
        mentor_detail = []
        try:
            get_mentor = self.c.execute("SELECT name, surname, email, date_of_birth, city, phone FROM Mentor"
                                         " WHERE name = '{}' and surname = '{}'".format(name, surname))
            for item in get_mentor:
                mentor_detail.append(item)
            self.conn.commit()
            return mentor_detail
        except sqlite3.OperationalError as w:
            print("Cant get student {}".format(w))