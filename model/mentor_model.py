import sqlite3


class Mentor:
    def get_list_of_mentors(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()
        mentor_list = []
        for item in self.c.execute("SELECT * FROM Mentor"):
            mentor_list.append(item)
        print(mentor_list)

    def add_mentor(self, *args):
        try:
            self.conn.execute("INSERT INTO Mentor VALUES (NULL,'{}','{}','{}','{}')".format(*args))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def remove_mentor_from_database(self, mentor_id):
        try:
            self.c.execute("DELETE FROM Mentor WHERE id={}".format(mentor_id))
            self.conn.commit()
        except sqlite3.OperationalError:
            print("Cant remove Table from database")


c = Mentor()

c.get_list_of_mentors()
c.add_mentor("Imie", "BBBBB", "CCCCCCC", "XD")
c.get_list_of_mentors()
