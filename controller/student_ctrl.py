from model.student_model import StudentModel
from controller.user_ctrl import User

class Student(User):

    def __init__(self, name, surname, email, date_of_birth, city, phone, attendance_level, group_id, student_card):
        super().__init__(name, surname, email, date_of_birth, city, phone)
        self.attendance_level = attendance_level
        self.group_id = group_id
        self.student_card = student_card


    def get_student_grades(self):
        return StudentModel.get_student_grades(self.get_full_name())

    def get_student_overall_attendance(self):
        return self.attendance_level
    @staticmethod
    def add_card(card_to_add, name, surname):
        model = StudentModel()
        model.add_card(card_to_add, name, surname)


    @staticmethod
    def get_students_list():
        model = StudentModel()
        list_of_students = model.get_list_of_students()
        return list_of_students

    @staticmethod
    def get_student_details(student_name, student_surname):
        model = StudentModel()
        student_details = model.get_student_detail(student_name, student_surname)
        return student_details

    @staticmethod
    def check_student_in_db_by_id(student_id):
        """
        check if student exists
        :param student_id:
        :return: boolean
        """
        return StudentModel.check_student_in_db_by_id_model(student_id)

    @staticmethod
    def remove_student_from_data_base(name, surname):
        model = StudentModel()
        model.remove_student_from_database(name, surname)

    @staticmethod
    def add_student(name, surname, email, date_of_birth, city, phone):
        model = StudentModel()
        model.add_student(name, surname, email, date_of_birth, city, phone)

    @staticmethod
    def edit_student(cur_name, cur_surname, name, surname, email, date_of_birth, city, phone):
        model = StudentModel()
        model.edit_student(cur_name, cur_surname, name, surname, email, date_of_birth, city, phone)
