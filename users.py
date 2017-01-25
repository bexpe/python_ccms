class User:
    def __init__(self, name, surname, id=0):
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

    @classmethod
    def list_to_csv(cls):
        table = cls.objects_to_list(cls)
        with open(cls.FILE, 'w') as file:
            for record in table:
                row = ','.join(record)
                file.write(row + "\n")


class Student(User):
    _students_list = []
    FILE = 'data/students.csv'

    def __init__(self, name, surname):
        super().__init__(name, surname)

        self.id = len(self._students_list) + 1
        self._students_list.append(self)
        self.grades = {}

    def objects_to_list(self):
        list_to_write = []

        for student in self._students_list:
            list_to_write.append([str(student.id), student.name, student.surname])
        return list_to_write

    @classmethod
    def save_students_csv(cls):
        cls.list_to_csv()

    @classmethod
    def load_students_csv(cls):

        import csv
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')

            for line in reader:
                Student(line[1], line[2])


class Employee(User):
    _employee_list = []
    FILE = 'data/employees.csv'

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.id = len(self._employee_list) + 1

        if self.__class__ == Employee:
            self._employee_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for person in self._employee_list:
            list_to_write.append([str(person.id), person.name, person.surname])
        return list_to_write

    @classmethod
    def save_employees_csv(cls):
        cls.list_to_csv()

    @classmethod
    def load_employees_csv(cls):

        import csv
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Employee(line[1], line[2])


class Manager(Employee):
    _manager_list = []
    FILE = 'data/managers.csv'

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.id = len(self._manager_list) + 1
        self._manager_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for person in self._manager_list:
            list_to_write.append([str(person.id), person.name, person.surname])
        return list_to_write

    @classmethod
    def save_manager_csv(cls):
        cls.list_to_csv()

    @classmethod
    def load_manager_csv(cls):
        import csv
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Manager(line[1], line[2])


class Mentor(Employee):
    _mentor_list = []
    FILE = 'data/mentors.csv'

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.id = len(self._mentor_list) + 1
        self._mentor_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for person in self._mentor_list:
            list_to_write.append([str(person.id), person.name, person.surname])
        return list_to_write

    @classmethod
    def save_mentor_csv(cls):
        cls.list_to_csv()

    @classmethod
    def load_mentor_csv(cls):
        import csv
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Mentor(line[1], line[2])


class Attedance:
    pass

