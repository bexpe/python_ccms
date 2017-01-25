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

    def edit_student(self, option):
        option = input('Choose what would you like to edit: 1. name \n, 2. surname \n, 3. grade \n, 4. date_of_birth \n, 5. city \n, 6. phone \n, 7. all')
        if option == '1':
            new_name = input('Please type new name: ')
            self.name = new_name
        if option == '2':
            new_surname = input('Please type new surname: ')
            self.surname = new_surname
        if option == '3':
            new_grade = input('Please type new grade: ')
            self.grade = new_grade
        if option == '4':
            new_date_of_birth = input('Please type new date of birth: ')
            self.date_of_birth = new_date_of_birth
        if option == '5':
            new_city = input('Please type new city: ')
            self.city = new_city
        if option == '6':
            new_phone = input('Please type new phone: ')
            self.phone = new_phone
        if option == '7':
            new_name = input('Please type new name: ')
            new_surname = input('Please type new surname: ')
            new_grade = input('Please type new grade: ')
            new_date_of_birth = input('Please type new date of birth: ')
            new_city = input('Please type new city: ')
            new_phone = input('Please type new phone: ')
            self.name = new_name
            self.surname = new_surname
            self.grade = new_grade
            self.date_of_birth = new_date_of_birth
            self.city = new_city
            self.phone = new_phone


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
    def __init__(self, name, surname, date_of_birth, city, phone):
        super().__init__(name, surname, date_of_birth, city, phone)
        self.id = len(self._employee_list) + 1
        self._employee_list.append(self)


class Manager(Employee):
    _manager_list = []
    def __init__(self, name, surname, date_of_birth, city, phone):
        super().__init__(name,surname, date_of_birth, city, phone)
        self.id = len(self._manager_list) + 1
        self._manager_list.append(self)


class Mentor(Employee):
    _mentor_list = []
    def __init__(self, name, surname, date_of_birth, city, phone):
        super().__init__(name, surname, date_of_birth, city, phone)
        self.id = len(self._mentor_list) + 1
        self._mentor_list.append(self)

class Attedance:
    pass

    #def check_attendence(self):
        #for student in _student_attendence_list

user = User('Tomasz', 'Bujakowski')
a = User("bla", "bla")
b = User('blaaaa', 'blaaaaaa')
student = Student('Ania', 'Gaj', '10-10-2000', 'Cracow', '122333555')
print(student.phone)

