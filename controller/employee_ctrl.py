from model.employee_model import Employee_model


class Employee(User):
    def __init__(self, name, surname, email, date_of_birth, city, phone):
        super().__init__(name, surname, email, date_of_birth, city, phone)


