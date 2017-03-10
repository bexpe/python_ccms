from model.database import Database
from model.user import User

class Employee(User):
    def __init__(self,user_id, name, surname, email, date_of_birth, city, phone, login):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)

    @classmethod
    def get_employee_by_id(cls, idx):
        db = Database()
        query = """SELECT * FROM Employee WHERE id =(?)"""
        person = db.get(query, (idx,))[0]
        print(person)
        new_employee = Employee(person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7])
        return new_employee

    def get_employee_details(self, idx):
        return self.__dict__

    @classmethod
    def get_list_of_employees(cls):
        list_of_employees = []
        db = Database()
        query = """SELECT * FROM Employee;"""
        for person in db.get(query):
            person_object = Employee(person[0], person[1], person[2], person[3], person[4], person[5], person[6],
                                   person[7])
            list_of_employees.append(person_object)

        db.close()
        return list_of_employees

    def save(self):
        db = Database()
        values = (
        self.name, self.surname, self.email, self.date_of_birth, self.city, self.phone, self.login, self.user_id)

        if not self.user_id:
            values = values[:-1]
            query = """INSERT INTO Employee(Name, Surname, Email, Date_of_birth, City, Phone, Login) VALUES (?,?,?,?,?,?,?);"""
        else:
            query = """UPDATE Employee SET Name=(?), Surname=(?), Email=(?), Date_of_birth=(?), City=(?), Phone=(?), Login=(?) WHERE id =(?);"""

        db.set(query, values)
        db.close()
