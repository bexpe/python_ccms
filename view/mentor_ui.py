from assigments import Assigment
from attendance import Attendance


class MentorUI(EmployeeUI):
    """There we are showing all Mentor options"""

    def __init__(self, mentor):
        super().__init__(mentor)

    def show_mentor_menu(self):
        """There we are showing mentor menu"""
        while True:
            print(
                "\n/---------------------"
                "\n| Mentor menu:"
                "\n| (1) Show student list"
                "\n| (2) Add assignment"
                "\n| (3) Grade assignment"
                "\n| (4) Set attendance"
                "\n| (5) Edit student"
                "\n| (6) Remove student"
                "\n| (7) Add student"
                "\n| (8) Check attendance"
                "\n| (0) Exit"
                "\n\---------------------"
            )
            mentor_option = input("Choose ur option:")
            if mentor_option == "1":
                self.show_student_list()
            elif mentor_option == "2":
                self.add_assignment()
            elif mentor_option == "3":
                self.grade_assignment()
            elif mentor_option == "4":
                self.set_attendance()
            elif mentor_option == "5":
                self.edit_student()
            elif mentor_option == "6":
                self.remove_student()
            elif mentor_option == "7":
                self.add_student()
            elif mentor_option == "8":
                self.check_attendance()
            elif mentor_option == "0":
                break
            else:
                print("You need to choose from options: ")

    @staticmethod
    def add_assignment():
        """There we are adding assignment"""
        assigment_name = input("Write new assignment name: ")
        description = input("Write description for new assignment: ")
        Assigment(assigment_name, description)

    @staticmethod
    def grade_assignment():
        """There we are grade assignment"""
        assignment_to_find = input("Write assignment name You wanna grade: ")
        assigment = Assigment.get_assigment_by_name(assignment_to_find)
        student_id = input("Write student id")
        print("Student answer: ", assigment.get_student_solution_link(student_id))
        new_grade = input("Write new rate for student")
        assigment.grade_student_answer(student_id, new_grade)

    @staticmethod
    def set_attendance():
        """There we are setting student attendance"""
        print(Student.get_student_list())
        Attendance.set_attendance()

    @staticmethod
    def check_attendance():
        """Print students list and particular student attendance"""
        print(Student.get_student_list())
        Attendance.print_attendance_percentage()

    @staticmethod
    def edit_student():
        print(Student.get_student_list())
        student_id = input("Insert student id: ")
        student = Student.get_student_from_list_by_id(student_id)
        if student:
            student.edit_user()
            print("*** Student edited ***")
        else:
            print("*** Student not found ***")

    @staticmethod
    def add_student():
        """There we are adding student to codecool"""
        name = input("Write student name: ")
        surname = input("Write student surname: ")
        email = input("Write student email: ")
        date_of_birth = input("Write student date of birth: ")
        city = input("Write student city: ")
        phone = input("Write student phone: ")
        new_student = Student(name, surname, email, date_of_birth, city, phone, attendance_level=0)

    @staticmethod
    def remove_student():
        """There we are removing student by his id"""
        student_id = input("Write me student id: ")
        Student.remove_student_from_list(student_id)