from model.employee_model import Employee_model
from controller.user_ctrl import User

class Employee(User):
    def __init__(self, name, surname, email, date_of_birth, city, phone):
        super().__init__(name, surname, email, date_of_birth, city, phone)

    @staticmethod
    def get_employees_list():
        model = Employee_model()
        list_of_employees = model.get_list_of_employees()
        return list_of_employees
