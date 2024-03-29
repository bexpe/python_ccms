import random
import csv
import hashlib


class User:

    def __init__(self, name, surname, email, date_of_birth, city, phone, password=None):
        # if not name or not surname or not email:
        #     raise ValueError("Name, surname and email can't be empty")

        self.name = name
        self.surname = surname
        self.username = self.name[:2] + self.surname[:3]
        # if '@' not in email:
        #     raise NameError("Invalid email")
        self.email = email
        if password is None:
            self.password = self.username.lower()
        else:
            self.password = password
        self.phone = phone
        self.city = city
        self.date_of_birth = date_of_birth

    def get_email(self):
        """
        This method gets an users email
        :return: users email as an object
        """
        return self.email

    def get_password(self):
        """
        This method gets an users password.
        :return: users password as an object
        """
        return self.password

    def change_password(self, new_password):
        """
        Changes an old password

        :param new_password:

        :return: new_password
        """
        self.password = new_password

    @classmethod
    def get_students_objects(cls):
        """
        :return: list of students as a list of objects
        """
        return cls._students_list

    @classmethod
    def list_to_csv(cls):
        """
        Write lists with objects' data to file
        :return: None
        """
        table = cls.objects_to_list()
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

    def edit_user(self):
        """
        Edit student object.
        :return: none
        """
        option = input('Choose what would you like to edit: \n1. name \n, 2. surname \n, 3. date_of_birth \n,'
                       ' 4. city \n, 5. phone \n, 6. all ')
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

    @staticmethod
    def show_list(to_print_list):
        """
        Returns a list as a string with users depending on the class we choose

        :param to_print_list:

        :return: string
        """
        # transposition of list to print, for easy access to columns
        transposed_to_print_list = [list(x) for x in zip(*to_print_list)]

        # evaluate lengths of strings in columns for getting longest strings, to determine columns widths
        columns_widths = []
        for line in transposed_to_print_list:
            max_width = 0
            for item in line:
                if len(str(item)) > max_width:
                    max_width = len(str(item)) + 2
            columns_widths.append(max_width)

        table_str = ""  # string with content of table
        # generate strings for top and bottom of table, and row separator
        pauses = "-" * (sum(columns_widths) + len(to_print_list[0]) - 1)  # create of string with '-' for printing (---)
        top = "/{}\\\n".format(pauses)  # top row of table /----\
        bot = "\\{}/\n".format(pauses)  # bottom row       \----/

        # generate separator row |---|----------|-----| ....
        separator = "|"

        for item in columns_widths:
            separator += '{:^{}}|'.format("-" * (columns_widths[columns_widths.index(item)]),
                                          columns_widths[columns_widths.index(item)] - 1)

        for line in to_print_list:
            i = 0
            table_str += '|'
            for item in line:  # print every item from list from table in format: | column | column | col | ...
                table_str += '{:^{}}|'.format(item, columns_widths[i])
                i += 1

            if line != to_print_list[-1]:  # adds separator after row, except last row (bottom row is adding later)
                table_str += "\n{}\n".format(separator)

        return "{}{}\n{}".format(top, table_str, bot)


class Student(User):
    _students_list = []
    FILE = 'data/students.csv'

    def __init__(self, name, surname, email, date_of_birth, city, phone, attendance_level, id=None, password=None):
        super().__init__(name, surname, email, date_of_birth, city, phone)
        if id is None:
            self.id = User.generate_random(Student._students_list)
        else:
            self.id = id
        if password is None:
            hash_object = hashlib.md5(self.username.lower().encode())
            self.password = hash_object.hexdigest()
        else:
            self.password = password
        self.attendance_level = attendance_level

        self._students_list.append(self)

    @classmethod
    def student_list_basics(cls):
        student_basics_list = []
        for student in cls._students_list:
            student_basics_list.append('\n name: {} surname: {} email: {}'.format(
                student.name, student.surname, student.email))
        return "".join(student_basics_list)

    @classmethod
    def save_students_csv(cls):
        """
        Runs list_to_csv for saving list to file
        :return: None
        """

        cls.list_to_csv()

    @classmethod
    def load_students_csv(cls):
        """
        Read data from file and runs init for every line in file
        :return: None
        """

        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')

            for line in reader:
                Student(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])

    @classmethod
    def get_student_from_list_by_id(cls, student_id):
        """
        Returns student object from list.
        :param student_id:
        :return: student: object
        """
        for student in cls._students_list:
            if student.get_student_id() == student_id:
                return student

    @classmethod
    def remove_student_from_list(cls, student_id):
        """
        Remove student object from list.
        :param student_id:
        :return: none
        """
        for student in cls._students_list:
            if student.get_student_id() == student_id:
                cls._students_list.remove(student)

    @classmethod
    def get_student_list(cls):
        """
        Generates string with string from shapes object list.
        :return: str: string with table to print, or information if list is empty
        """
        list_to_print = cls.get_list_to_print()
        table = cls.show_list(list_to_print)
        return table

    @classmethod
    def get_list_to_print(cls):
        """Returns list with list made from objects data"""
        header_row = ['id', 'Name', 'Surname', 'email', 'Date_of_birth', 'Attendance level', 'Phone number']
        to_print_list = [header_row]
        for student in cls._students_list:
            to_print_list.append(
                [student.id, student.name, student.surname, student.email, student.date_of_birth,
                 student.attendance_level,
                 student.phone])
        return to_print_list

    @classmethod
    def get_student_details(cls, student):
        """
        Returns student object.
        :param student:
        :return: student: object
        """
        return cls.get_student_from_list_by_id(student)

    @classmethod
    def get_students_objects(cls):
        """
        Returns student list of objects.
        :return: student list of objects
        """
        return cls._students_list

    @classmethod
    def objects_to_list(cls):
        """
        Returns student list of strings
        :return: student info: list
        """
        list_to_write = []

        for student in cls._students_list:
            list_to_write.append(
                [student.name, student.surname, student.email, student.date_of_birth, student.city, str(
                    student.phone), str(student.attendance_level), student.id, student.password])
        return list_to_write

    def get_student_id(self):
        return self.id


class Employee(User):
    _employee_list = []
    FILE = 'data/employees.csv'

    def __init__(self, name, surname, email, date_of_birth, city, phone, id=None, password=None):
        """
        Initialize Employee object
        :param name:
        :param surname:
        :param email:
        :param date_of_birth:
        :param city:
        :param phone:
        :param id:
        :param password:
        """
        super().__init__(name, surname, email, date_of_birth, city, phone)

        if id is None:
            self.id = User.generate_random(Employee._employee_list)
        else:
            self.id = id

        if password is None:
            hash_object = hashlib.md5(self.username.lower().encode())
            self.password = hash_object.hexdigest()
        else:
            self.password = password

        if self.__class__ == Employee:
            self._employee_list.append(self)

    @classmethod
    def objects_to_list(cls):
        """
        Returns employee list of strings
        :return: employee info: list
        """
        employee_list = []

        for person in cls._employee_list:
            employee_list.append(
                [person.name, person.surname, person.email, person.date_of_birth, person.city, person.phone, person.id,
                 person.password])
        return employee_list

    @classmethod
    def save_employees_csv(cls):
        """
        Saves list of employees objects to csv.
        :return: none
        """
        cls.list_to_csv()

    @classmethod
    def load_employees_csv(cls):
        """
        Loads from csv and creates Employee objects.
        :return: None
        """
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])

    @classmethod
    def get_employees_objects(cls):
        """
        Gives employees objects list

        :return: list of employees objects
        """
        return cls._employee_list

    @classmethod
    def get_employees_objects(cls):
        """
        :return: employee list of objects
        """
        return cls._employee_list


class Manager(Employee):
    _manager_list = []
    FILE = 'data/managers.csv'

    def __init__(self, name, surname, email, date_of_birth, city, phone, id=None, password=None):
        super().__init__(name, surname, email, date_of_birth, city, phone)

        if id is None:
            self.id = User.generate_random(Manager._manager_list)
        else:
            self.id = id

        if password is None:
            hash_object = hashlib.md5(self.username.lower().encode())
            self.password = hash_object.hexdigest()
        else:
            self.password = password

        self._manager_list.append(self)

    @classmethod
    def objects_to_list(cls):
        """
        Convert objects from objects list to list of lists

        :return: list: list with lists with persons' data
        """

        list_to_write = []

        for person in cls._manager_list:
            list_to_write.append(
                [person.name, person.surname, person.email, person.date_of_birth, person.city, person.phone, person.id,
                 person.password])
        return list_to_write

    @classmethod
    def save_manager_csv(cls):
        """
        Runs list_to_csv for saving list to file
        :return: None
        """
        cls.list_to_csv()

    @classmethod
    def load_manager_csv(cls):
        """
        Read data from file and runs init for every line in file
        :return: None
        """
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Manager(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])

    @classmethod
    def get_managers_objects(cls):
        return cls._manager_list

    @classmethod
    def get_managers_objects(cls):
        """
        :return: list of managers objects
        """
        return cls._manager_list


class Mentor(Employee):
    _mentor_list = []
    FILE = 'data/mentors.csv'

    def __init__(self, name, surname, email, date_of_birth, city, phone, id=None, password=None):
        super().__init__(name, surname, email, date_of_birth, city, phone)

        if id is None:
            self.id = User.generate_random(Mentor._mentor_list)
        else:
            self.id = id

        if password is None:
            hash_object = hashlib.md5(self.username.lower().encode())
            self.password = hash_object.hexdigest()
        else:
            self.password = password

        self._mentor_list.append(self)

    @classmethod
    def objects_to_list(cls):
        """
        Convert objects from objects list to list of lists

        :return: list: list with lists with persons' data
        """

        list_to_write = []

        for person in cls._mentor_list:
            list_to_write.append(
                [person.name, person.surname, person.email, person.date_of_birth, person.city, person.phone, person.id,
                 person.password])
        return list_to_write

    @classmethod
    def mentor_list_basics(cls):
        mentor_basics_list = []
        for mentor in cls._mentor_list:
            mentor_basics_list.append('\n name: {} surname: {} email: {}'.format(
                mentor.name, mentor.surname, mentor.email))
        return "".join(mentor_basics_list)

    @classmethod
    def get_mentor_from_list_by_id(cls, mentor_id):
        for mentor in cls._mentor_list:
            if mentor.id == mentor_id:
                return mentor

    @classmethod
    def remove_mentor_from_list(cls, mentor_id):
        for mentor in cls._mentor_list:
            if mentor.id == mentor_id:
                cls._mentor_list.remove(mentor)

    @classmethod
    def load_mentor_csv(cls):
        """
        Read data from file and runs init for every line in file
        :return: None
        """
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Mentor(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])

    @classmethod
    def save_mentor_csv(cls):
        """
        Runs list_to_csv for saving list to file
        :return: None
        """
        cls.list_to_csv()

    def edit_mentor(cls):
        option = input('Choose what would you like to edit: 1. name \n, 2. surname \n, 3. date_of_birth \n, 4. city \n,'
                       ' 5. phone \n, 6. all')
        if option == '1':
            new_name = input('Please type new name: ')
            cls.name = new_name
        if option == '2':
            new_surname = input('Please type new surname: ')
            cls.surname = new_surname
        if option == '3':
            new_date_of_birth = input('Please type new date of birth: ')
            cls.date_of_birth = new_date_of_birth
        if option == '4':
            new_city = input('Please type new city: ')
            cls.city = new_city
        if option == '5':
            new_phone = input('Please type new phone: ')
            cls.phone = new_phone
        if option == '6':
            new_name = input('Please type new name: ')
            new_surname = input('Please type new surname: ')
            new_date_of_birth = input('Please type new date of birth: ')
            new_city = input('Please type new city: ')
            new_phone = input('Please type new phone: ')
            cls.name = new_name
            cls.surname = new_surname
            cls.date_of_birth = new_date_of_birth
            cls.city = new_city
            cls.phone = new_phone

    @classmethod
    def get_mentor_list(cls):
        """Returns string with table to print"""
        list_to_print = cls.get_list_to_print()
        table = cls.show_list(list_to_print)
        return table

    @classmethod
    def get_list_to_print(cls):
        """Returns list with list made from objects data"""
        header_row = ['Name', 'Surname', 'email', 'Date_of_birth', 'Phone number']
        to_print_list = [header_row]
        for mentor in cls._mentor_list:
            to_print_list.append(
                [mentor.name, mentor.surname, mentor.email, mentor.date_of_birth, mentor.phone])
        return to_print_list

    @classmethod
    def get_mentors_objects(cls):
        return cls._mentor_list


if __name__ == '__main__':
    mm = Mentor('Mentor', 'Mentorowski', 'mentor@cc', '1960-12-12', 'City', '333-232-111')
    student = Student('Student', 'Studencki', 'student@cc', '1990-1211', 'City', '32-32-1231', 0)
    mena = Manager('Jurek', 'Jerzy', 'jurek@cc', '1960-12-12', 'City', '312-321-321')
    emp = Employee('Employee', "Emplo", 'emp@cc', '1970-12-23', 'City', '231-231-323')
    Mentor.save_mentor_csv()
    Student.save_students_csv()
    Manager.save_manager_csv()
    Employee.save_employees_csv()
