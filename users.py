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

    def __init__(self, name, surname, date_of_birth, city, phone, attendence_level):
        super().__init__(name, surname, date_of_birth, city, phone)
        self.id = len(self._students_list) + 1
        self._students_list.append(self)
        self.attendence_level = attendence_level
        self.grades = {}

    def objects_to_list(self):
        list_to_write = []

        for student in self._students_list:
            list_to_write.append([str(student.id), student.name, student.surname, student.date_of_birth, student.city,
                                  str(student.phone), str(student.attendence_level)])
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
                Student(line[1], line[2], line[3], line[4], line[5], line [6])

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

    FILE = 'data/employees.csv'

    def __init__(self, name, surname, date_of_birth, city, phone):
        super().__init__(name, surname, date_of_birth, city, phone)
        self.id = len(self._employee_list) + 1

        if self.__class__ == Employee:
            self._employee_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for person in self._employee_list:
            list_to_write.append([str(person.id), person.name, person.surname, person.date_of_birth, person.city, person.phone])
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
                Employee(line[1], line[2], line[3], line[4], line[5])


class Manager(Employee):
    _manager_list = []
    FILE = 'data/managers.csv'

    def __init__(self, name, surname, date_of_birth, city, phone):
        super().__init__(name, surname, date_of_birth, city, phone)
        self.id = len(self._manager_list) + 1
        self._manager_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for person in self._manager_list:
            list_to_write.append([str(person.id), person.name, person.surname, person.date_of_birth, person.city, person.phone])
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
                Manager(line[1], line[2], line[3], line[4], line[5])


class Mentor(Employee):
    _mentor_list = []
    FILE = 'data/mentors.csv'

    def __init__(self, name, surname, date_of_birth, city, phone):
        super().__init__(name, surname, date_of_birth, city, phone)
        self.id = len(self._mentor_list) + 1
        self._mentor_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for person in self._mentor_list:
            list_to_write.append([str(person.id), person.name, person.surname, person.date_of_birth, person.city, person.phone])
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
                print(line)
                Mentor(line[1], line[2], line[3], line[4], line[5])


class Attedance:
    pass


    # def check_attendence(self):
    # for student in _student_attendence_list

Student.load_students_csv()
Manager.load_manager_csv()
Mentor.load_mentor_csv()
Employee.load_employees_csv()
m = Manager('Jurek','JurekSurname', '12-21-1231', 'Cracow', '11111111')

men = Mentor('Mentor','MentorName', '12-21-1231', 'Cracow', '11111111')
emp = Employee('Employ','EmployName', '12-21-1231', 'Cracow', '11111111')
user = User('Tomasz', 'Bujakowski', '12-21-1231', 'Cracow', '11111111')
student = Student('Ania', 'Gaj', '10-10-2000', 'Cracow', '122333555', 0)
# print(student.phone)
#
Student.save_students_csv()
Manager.save_manager_csv()
Mentor.save_mentor_csv()
Employee.save_employees_csv()
