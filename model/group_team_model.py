import sqlite3

class Team:

    def __init__(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()

    def add_new_group(self, *args):
        try:
            self.conn.execute("INSERT INTO Groups VALUES (NULL,'{}','{}','{}')".format(*args))
            self.conn.commit()
            print('New group is added')
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def display_all_groups(self):
        groups_list = []
        for item in self.c.execute("SELECT * FROM Groups"):
            groups_list.append(item)
        print(groups_list)

    def add_student_to_team(self, student_name, group_id):
        try:
            self.conn.execute("UPDATE Groups SET student_list = student_list || ',' || '{}' WHERE ID = {}".format(student_name, group_id))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def close_database(self):
        self.conn.close()

c = Team()
c.add_new_group('Stefany','',1)
c.add_student_to_team('Darek', 2)
c.display_all_groups()