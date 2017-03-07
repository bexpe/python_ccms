from model.database import Database
from model.user import User

class Employee(User):
    def __init__(self,user_id, name, surname, email, date_of_birth, city, phone, login):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)

    def get_employee_by_id(self, idx):
        db = Database()
        query = """SELECT * FROM Employee WHERE id =(?)"""
        person = db.get(query, (idx,))
        new_employee = Employee(person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7])
        return new_employee

    @classmethod
    def get_list_of_employees(cls):
        list_of_employees = []
        db = Database()
        query = """SELECT * FROM Employee;"""
        for person in db.get(query):
            person_object = Employee(person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7])
            list_of_employees.append(person_object)

        db.close()
        return list_of_employees

    def edit_employee(self, employee_object):
        db = Database()
        query = """UPDATE Employee SET Name=(?), Surname=(?), Email=(?), Date_of_birth=(?), City=(?), Phone=(?), Login=(?) WHERE id =(?);"""
        db.get(query, (
                        employee_object.name,
                        employee_object.surname,
                        employee_object.email,
                        employee_object.date_of_birth,
                        employee_object.city,
                        employee_object.phone,
                        employee_object.login,
                        employee_object.user_id
                        )
                )

    def add_new_employee(self, employee_object):
        db = Database()
        query = """INSERT INTO Employee(Name, Surname, Email, Date_of_birth, City, Phone, Login) VALUES (?,?,?,?,?,?,?);"""
        db.get(query, (
                        employee_object.name,
                        employee_object.surname,
                        employee_object.email,
                        employee_object.date_of_birth,
                        employee_object.city,
                        employee_object.phone,
                        employee_object.login,
                        employee_object.user_id
                        )
                )