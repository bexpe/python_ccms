class User:
    def __init__(self, name, surname):
        if len(name) == 0 or len(surname) == 0:
            raise ValueError('Name and surname cannot be empty.')

        self.name = name
        self.surname = surname

        self.username = self.name[:2] + self.surname[:3]
        self.password = self.username.lower()

    def change_password(self, new_password):
        self.password = new_password

    def set_name(self, new_name):
        self.name = new_name

    def set_surname(self, new_surname):
        self.surname = new_surname




class Student(User):
    pass


class Employee(User):
    pass


class Menager(Employee):
    pass


class Mentor(Employee):
    pass

user = User('', 'Bujakowski')
print(user.__dict__)