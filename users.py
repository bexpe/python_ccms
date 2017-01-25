class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

        self.username = self.name[:2] + self.surname[:3]
        self.password = self.username.lower()

class Student(User):
    pass


class Employee(User):
    pass


class Menager(Employee):
    pass


class Mentor(Employee):
    pass

user = User('Tomek', 'Bujakowski')
print(user.__dict__)