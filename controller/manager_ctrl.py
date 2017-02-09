from model.manager_model import Manager_model


class Manager(Employee):
    def __init__(self, name, surname, email, date_of_birth, city, phone):
        super().__init__(name, surname, email, date_of_birth, city, phone)