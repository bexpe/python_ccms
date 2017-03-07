import sqlite3


class Manager_model:

    def __init__(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()

    def get_list_of_managers(self):
        managers_list = []
        for item in self.c.execute("SELECT * FROM Manager"):
            managers_list.append(item)
        return managers_list