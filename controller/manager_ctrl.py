from model.manager_model import Manager_model
from controller.employee_ctrl import Employee


class Manager(Employee):
    def __init__(self, name, surname, email, date_of_birth, city, phone):
        super().__init__(name, surname, email, date_of_birth, city, phone)

    @staticmethod
    def get_managers_list():
        model = Manager_model()
        list_of_managers = model.get_list_of_managers()
        return list_of_managers