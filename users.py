class User:
    def __init__(self, name, surname):
        if len(name) == 0 or len(surname) == 0:
            raise ValueError('Name and surname cannot be empty.')
        self.id = len(self._user_list) + 1
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
    pass


class Employee(User):
    pass


class Menager(Employee):
    pass


class Mentor(Employee):
    pass

class Attedance:
    pass
    #def check_attendence(self):
        #for student in _student_attendence_list

user = User('Tomasz', 'Bujakowski')
a = User("bla", "bla")
b = User('blaaaa', 'blaaaaaa')
user.print_object()