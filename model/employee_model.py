import sqlite3


class Employee:

    def __init__(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()

    def get_list_of_employees(self):
        self.conn = sqlite3.connect("baza_danych.db")
        self.c = self.conn.cursor()
        employee_list = []
        for item in self.c.execute("SELECT * FROM Employee"):
            employee_list.append(item)
        return employee_list

    def add_employee(self, *args):
        try:
            self.conn.execute("INSERT INTO Employee VALUES (NULL,'{}','{}','{}','{}')".format(*args))
            self.conn.commit()
        except sqlite3.OperationalError as w:
            print("Cant add this {}".format(w))

    def remove_employee_from_database(self, employee_id):
        try:
            self.c.execute("DELETE FROM Employee WHERE id={}".format(employee_id))
            self.conn.commit()
        except sqlite3.OperationalError:
            print("Cant remove Table from database")

    def get_employee_detail(self, name, surname):
        employee_detail = []
        try:
            get_student = self.c.execute("SELECT name, surname, email, city, phone FROM Employee"
                                         " WHERE name = {} and surname = {}".format(name, surname))
            for item in get_student:
                employee_detail.append(item)
            self.conn.commit()
            return employee_detail

        except sqlite3.OperationalError as w:
            print("Cant get student {}".format(w))

    def edit_employee(self, employee_id, *args):
        try:
            self.c.execute("UPDATE Employee SET Name = '{}', Surname = '{}',Email = '{}',"
                           "City = '{}', Phone = '{}' WHERE ID = {}".format(*args, employee_id))
            self.conn.commit()

        except sqlite3.OperationalError as w:
            print("Cant edit mentor: {}".format(w))

    def close_database(self):
        self.conn.close()
