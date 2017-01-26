import random


class User:
    def __init__(self, name, surname, date_of_birth, city, phone, password=None):
        if len(name) == 0 or len(surname) == 0:
            raise ValueError('Name and surname cannot be empty.')

        self.name = name
        self.surname = surname
        self.username = self.name[:2] + self.surname[:3]
        if password == None:
            self.password = self.username.lower()
        else:
            self.password = password
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

    @staticmethod
    def generate_random(table):
        """
        Generates random and unique string. Used for id/key generation.

        Args:
            table: list containing keys. Generated string should be different then all of them

        Returns:
            Random and unique string
        """

        list_of_id = []
        for record in table:
            list_of_id.append(record.id)

        generated = ''

        special_char_index = list(range(33, 48)) + list(range(58, 59)) + list(range(60, 65)) \
                             + list(range(91, 97)) + list(range(124, 127))
        start = True
        max_len_id = 3
        while start:
            list_of_char = []
            new_id = ''

            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(str(chr(random.choice(special_char_index))))
            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(str(random.randint(0, 9)))
            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(chr(random.randint(97, 122)).upper())
            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(chr(random.randint(97, 122)))

            for i in range(len(list_of_char)):
                char = random.choice(list_of_char)
                new_id += char
                list_of_char.remove(char)
            if new_id not in list_of_id:
                generated += new_id
                start = False

        return generated


class Student(User):
    _students_list = []
    FILE = 'data/students.csv'

    def __init__(self, name, surname, date_of_birth, city, phone, attendance_level, id=None, password=None):
        super().__init__(name, surname, date_of_birth, city, phone)
        if id == None:
            self.id = User.generate_random(Student._students_list)
        else:
            self.id = id
        self.attendance_level = attendance_level
        self.grade = {}

        self._students_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for student in self._students_list:
            list_to_write.append([student.name, student.surname, student.date_of_birth, student.city,
                                  str(student.phone), str(student.attendance_level), student.id, student.password])
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
                Student(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])

    def edit_student(self):
        option = input('Choose what would you like to edit: 1. name \n, 2. surname \n, 3. grade \n, 4. date_of_birth\n,'
                       ' 5. city \n, 6. phone \n, 7. all')
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
        for student in cls._students_list:
            if student.id == id:
                return student

    @classmethod
    def remove_student_from_list(cls):
        cls.id = cls.id
        for student in cls._students_list:
            if student.id == cls.id:
                cls._students_list.remove(student)

    @classmethod
    def get_student_list(cls):
        return cls._students_list


class Employee(User):
    _employee_list = []
    FILE = 'data/employees.csv'

    def __init__(self, name, surname, date_of_birth, city, phone, id=None, password=None):
        super().__init__(name, surname, date_of_birth, city, phone)

        if id == None:
            self.id = User.generate_random(Employee._employee_list)
        else:
            self.id = id

        if password == None:
            self.password = self.username
        else:
            self.password = password

        if self.__class__ == Employee:
            self._employee_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for person in self._employee_list:
            list_to_write.append(
                [person.name, person.surname, person.date_of_birth, person.city, person.phone, person.id,
                 person.password])
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
                Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6])


class Manager(Employee):
    _manager_list = []
    FILE = 'data/managers.csv'

    def __init__(self, name, surname, date_of_birth, city, phone, id=None, password=None):
        super().__init__(name, surname, date_of_birth, city, phone)

        if id == None:
            self.id = User.generate_random(Manager._manager_list)
        else:
            self.id = id

        if password == None:
            self.password = self.username.lower()
        else:
            self.password = password

        self._manager_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for person in self._manager_list:
            list_to_write.append(
                [person.name, person.surname, person.date_of_birth, person.city, person.phone, person.id,
                 person.password])
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
                Manager(line[0], line[1], line[2], line[3], line[4], line[5], line[6])


class Mentor(Employee):
    _mentor_list = []
    FILE = 'data/mentors.csv'

    def __init__(self, name, surname, date_of_birth, city, phone, id=None, password=None):
        super().__init__(name, surname, date_of_birth, city, phone)

        if id == None:
            self.id = User.generate_random(Mentor._mentor_list)
        else:
            self.id = id

        if password == None:
            self.password = self.username
        else:
            self.password = password

        self._mentor_list.append(self)

    def objects_to_list(self):
        list_to_write = []

        for person in self._mentor_list:
            list_to_write.append(
                [person.name, person.surname, person.date_of_birth, person.city, person.phone, person.id,
                 person.password])
        return list_to_write

    @classmethod
    def get_mentor_from_list_by_id(cls, id):
        for mentor in cls._mentor_list:
            if mentor.id == id:
                return mentor

    @classmethod
    def remove_mentor_from_list(cls, id):
        for mentor in cls._mentor_list:
            if mentor.id == id:
                cls._mentor_list.remove(mentor)

    @classmethod
    def load_mentor_csv(cls):
        import csv
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Mentor(line[0], line[1], line[2], line[3], line[4], line[5], line[6])

    @classmethod
    def save_mentor_csv(cls):
        cls.list_to_csv()

    def edit_mentor(self):
        option = input('Choose what would you like to edit: 1. name \n, 2. surname \n, 3. date_of_birth \n, 4. city \n,'
                       ' 5. phone \n, 6. all')
        if option == '1':
            new_name = input('Please type new name: ')
            self.name = new_name
        if option == '2':
            new_surname = input('Please type new surname: ')
            self.surname = new_surname
        if option == '3':
            new_date_of_birth = input('Please type new date of birth: ')
            self.date_of_birth = new_date_of_birth
        if option == '4':
            new_city = input('Please type new city: ')
            self.city = new_city
        if option == '5':
            new_phone = input('Please type new phone: ')
            self.phone = new_phone
        if option == '6':
            new_name = input('Please type new name: ')
            new_surname = input('Please type new surname: ')
            new_date_of_birth = input('Please type new date of birth: ')
            new_city = input('Please type new city: ')
            new_phone = input('Please type new phone: ')
            self.name = new_name
            self.surname = new_surname
            self.date_of_birth = new_date_of_birth
            self.city = new_city
            self.phone = new_phone


class Attendance:
    _attendance_list = []
    FILE = 'data/attendance.csv'

    def __init__(self, student_id, date, attendance):
        self.student_id = student_id
        self.date = date
        self.attendance = attendance

    @classmethod
    def set_attendance(cls):
        student_id = input('Insert student id')
        date = input('Insert date: DD:MM:YYYY')
        option = input('A= present, B= late C= not there')
        if option == 'A':
            attendance = 'present'
        elif option == 'B':
            attendance = 'late'
        elif option == 'C':
            attendance = 'absent'
        else:
            raise KeyError("There is no such option.")
        student = Student.get_student_from_list_by_id(student_id)
        cls._attendance_list.append(Attendance(student.id, date, attendance))

    @classmethod
    def get_student_attendance_list(cls):
        cls._attendance_list

    @classmethod
    def check_attendance_by_id(cls, student_id):
        student_attendance_list = []
        student = Student.get_student_from_list_by_id(student_id.id)
        for attendance in cls._attendance_list:
            if attendance.student_id == student.id:
                student_attendance_list.append(attendance)
        return student_attendance_list

    @classmethod
    def count_attendance_values(cls, student_id):
        values_attendance_by_id_dict = {'id': 0, 'day_sum': 0, 'present': 0, 'late': 0, 'absent': 0}
        attendance_list = cls.check_attendance_by_id(student_id)
        values_attendance_by_id_dict['id'] = student_id.id
        for attendance in attendance_list:
            values_attendance_by_id_dict['day_sum'] += 1
            if attendance.attendance == 'present':
                values_attendance_by_id_dict['present'] += 1
            elif attendance.attendance == 'late':
                values_attendance_by_id_dict['late'] += 1
            elif attendance.attendance == 'absent':
                values_attendance_by_id_dict['absent'] += 1
        return values_attendance_by_id_dict

    @classmethod
    def print_attendance_percentage(cls):
        cls.set_attendance()
        student_id = input('Insert student id \n')
        student_id = Student.get_student_from_list_by_id(student_id)
        attendance_dict = cls.count_attendance_values(student_id)
        for key, value in attendance_dict.items():
            print('{} : {}' .format(key, value))

    def objects_to_list(self):
        list_to_write = []

        for item in self._attendance_list:
            list_to_write.append(
                [item.student_id, item.date, item.attendance])
        return list_to_write

    @classmethod
    def save_students_attendance_(cls):
        table = cls.objects_to_list(cls)
        with open(cls.FILE, 'w') as file:
            for record in table:
                row = ','.join(record)
                file.write(row + "\n")

    @classmethod
    def load_students_attendance_(cls):

        import csv
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')

            for line in reader:
                Attendance(line[0], line[1], line[2])
Student.load_students_csv()
Attendance.print_attendance_percentage()
