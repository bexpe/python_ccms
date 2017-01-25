import random

class User:
    def __init__(self, name, surname, date_of_birth, city, phone):
        if len(name) == 0 or len(surname) == 0:
            raise ValueError('Name and surname cannot be empty.')

        self.name = name
        self.surname = surname

        self.username = self.name[:2] + self.surname[:3]
        self.password = self.username.lower()
        self.phone = phone
        self.city = city
        self.date_of_birth = date_of_birth

    def change_password(self, new_password):
        self.password = new_password

class Student(User):
    _students_list = []

    def __init__(self, name, surname, date_of_birth, city, phone, attendence_level):
        super().__init__(name,surname, surname, date_of_birth, city, phone)
        self.id = len(self._students_list) + 1
        self._students_list.append(self)
        self.attendence_level = attendence_level

    @classmethod
    def load_student_csv(cls):
        pass

    @classmethod
    def save_students_csv(cls):
        pass

    def edit_student(self, student, ):
        if option == 'name':
            student.name = new_name
        if option == 'surname':
            student.surname = new_surname
        if option == 'grade':
            student.grade = new_grade

    @classmethod
    def get_student_from_list_by_id(cls, id):
        id = int(id)
        for student in cls._students_list:
            if int(student.id) == id:
                return student

    @classmethod
    def remove_student_from_list(cls, id):
        id = int(id)
        for student in cls._students_list:
            if int(student.id) == id:
                cls._students_list.remove(student)

    def get_student_id(self):
        return self.student.id


    @classmethod
    def get_student_list(cls):
        return cls._students_list

class Employee(User):
    _employee_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.id = len(self._employee_list) + 1
        self._employee_list.append(self)


class Manager(Employee):
    _manager_list = []
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.id = len(self._manager_list) + 1
        self._manager_list.append(self)


class Mentor(Employee):
    _mentor_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.id = len(self._mentor_list) + 1
        self._mentor_list.append(self)

class Attedance:
    pass

user = User('Tomasz', 'Bujakowski')
a = User("bla", "bla")
b = User('blaaaa', 'blaaaaaa')
student = Student('Ania', 'Gaj', '10-10-2000', 'Cracow', '122333555')
print(student.phone)

