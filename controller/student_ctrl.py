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