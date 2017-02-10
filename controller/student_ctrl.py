from model.student_model import StudentModel


class Student:

    def __init__(self, name, surname, email, date_of_birth, city, phone, attendance_level, group_name, student_card):
        super().__init__(name, surname, email, date_of_birth, city, phone)
        self.attendance_level = attendance_level
        self.group_name = group_name
        self.student_card = student_card

    def get_student_grades(self):
        return StudentModel.get_student_grades(self.get_full_name())

    def get_student_details(self):
        basic_data = self.get_details_basic()
        return basic_data + [self.attendance_level, self.group_name]

    def get_student_overall_attendance(self):
        return self.attendance_level

    def remove_student(self):
        StudentModel.remove_student(self.get_full_name())

    def add_card(self, card_to_add):
        self.student_card = card_to_add

    @staticmethod
    def get_students_list():
        list_of_students = StudentModel.get_students_list()

    @staticmethod
    def get_student_by_name(student_name):
        student_data = StudentModel.get_student_by_name(student_name)
        return Student(
            student_data[0],
            student_data[1],
            student_data[2],
            student_data[3],
            student_data[4],
            student_data[5],
            # attendance level,
            # group name
        )

    @staticmethod
    def check_student_in_db_by_id(student_id):
        """
        check if student exists
        :param student_id:
        :return: boolean
        """
        return StudentModel.check_student_in_db_by_id_model(student_id)

    @staticmethod
    def remove_student_from_data_base(student_name):
        StudentModel.remove_student_from_data_base(student_name)

    @staticmethod
    def add_new_student(name, surname, email, date_of_birth, city, phone):
        StudentModel.add_new_student(name, surname, email, date_of_birth, city, phone)
