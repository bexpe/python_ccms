import sqlite3

class Team:

    def __init__(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()

    def create_team(self, *args):
        try:
            self.conn.execute("INSERT INTO Groups VALUES (NULL,'{}','{}')".format(*args))
            self.conn.commit()
            print('New group is added')
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def display_all_groups(self):
        groups_list = []
        for item in self.c.execute("SELECT * FROM Groups"):
            groups_list.append(item)
        print(groups_list)

    def add_student_to_team(self, student_name):
        try:
            self.conn.execute("INSERT INTO Groups(name) VALUES ('{}')".format(student_name))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def edit_mentor(self, mentor_id, *args):
        try:
            self.c.execute("UPDATE Mentor SET Name = '{}', Surname = '{}',Email = '{}', Date_of_birth = '{}',"
                           "City = '{}', Phone = '{}' WHERE ID = {}".format(*args, mentor_id))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant edit mentor: {}".format(w))

    def close_database(self):
        self.conn.close()

t = Team()
t.create_team("zupa", "dupa")
t.display_all_groups()
t.add_student_to_team("zzz")
t.display_all_groups()