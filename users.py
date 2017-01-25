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

    def remove_from_list(self, object):
        self._user_list.remove(object)

    @classmethod
    def print_object(cls):
        for line in cls._user_list:
            print(line.name)

class Student(User):
    _students_list = []
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.id = len(self._students_list) + 1
        self._students_list.append(self)


class Employee(User):
    _manager_list = []
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.id = len(self._manager_list) + 1
        self._manager_list.append(self)


class Manager(Employee):
    _manager_list = []
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.id = len(self._manager_list) + 1
        self._manager_list.append(self)


class Mentor(Employee):
    _mentor_list = []
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.id = len(self._mentor_list) + 1
        self._mentor_list.append(self)

class Attedance:
    pass
