from users import *
from assigments import Assigment


class StudentUI():

    def __init__(self, student):
        self.student = student

    def show_student_menu(self):
        while True:
            print(
                "\n/---------------------"
                "\n| Student menu:"
                "\n| (1) Show my grades"
                "\n| (2) Show assignments"
                "\n| (3) Submit assignment"
                "\n| (0) Exit"
                "\n\---------------------"
            )
            user_choose = input('Your choose: ')
            if user_choose == "1":
                self.show_student_grade_ui()
            elif user_choose == "2":
                self.show_assigments_ui()
            elif user_choose == "3":
                self.submit_assigment_ui()
            elif user_choose == "0":
                quit()
            else:
                print("Bad choice. Enter correct value.")

    def show_student_grade_ui(self):
        student_grades = {}

        assigments_list = Assigment.get_assigments_list()
        for assigment in assigments_list:
            grade = assigment.get_student_grade(self.student.get_student_id())
            student_grades[assigment.get_assigment_name()] = grade

        student_grades_table = ["\n| {} : {} %".format(key, value) for key, value in student_grades.items()]

        print((
            "\n/---------------------"
            "\n| Your grades:"
            "{}"
            "\n\---------------------"
        ).format(
            ''.join(student_grades_table)
        ))

    def show_assigments_ui(self):
        assigments_list = Assigment.get_assigments_list()
        assigments_table = ["\n| {}".format(assigment.get_assigment_name()) for assigment in assigments_list]

        print((
            "\n/---------------------"
            "\n| Assigments:"
            "{}"
            "\n\---------------------"
        ).format(
            ''.join(assigments_table)
        ))

    def submit_assigment_ui(self):
        print(
            "\n/---------------------"
            "\n| Submit assigment"
            "\n|"
        )
        assigment_name = input('| Assigment name: ')
        assigment = Assigment.get_assigment_by_name(assigment_name)  # do poprawy
        if assigment:
            student_solution = input('| Insert your solution(github link): ')
            assigment.submit_assigment_answer(self.student.get_student_id(), student_solution)
            print(" *** Solution added *** ")
        else:
            print(" *** Assigment not found *** ")


class EmployeeUI:
    """There we are showing all employee options"""
    def __init__(self, employee):
        self.employee = employee

    def show_employee_menu(self):
        """There we are showing employee menu"""
        while True:
            print(
                "\n/---------------------"
                "\n| Employee menu:"
                "\n| (1) Show student list"
                "\n| (0) Exit"
                "\n\---------------------"
            )
            employee_options = input("Choose ur option: ")
            if employee_options == "1":
                self.show_student_list()
            elif employee_options == "0":
                quit()
            else:
                print("You need to choose from options")

    def show_student_list(self):
        """There we are showing student list"""
        print(Student.student_list_basics())
        employee_table_option = input("\n/---------------------"
                                      "\n| Employee menu:"
                                      "\n| (1) Show student details"
                                      "\n| (2) Return to menu"
                                      "\n| (0) Exit"
                                      "\n\---------------------\n")

        if employee_table_option == "1":
            self.show_student_details()
        elif employee_table_option == "2":
            self.show_employee_menu()
        elif employee_table_option == "0":
            quit()
        else:
            print("You need to choose from option")

    def show_student_details(self):
        """There we are showing student list with details"""
        print(Student.get_student_list())
        print("\n/---------------------"
              "\n| Employee menu:"
              "\n| (1) Return to menu"
              "\n| (0) Exit"
              "\n\---------------------")
        employee_option = input("Choose ur option: ")
        if employee_option == "1":
            self.show_employee_menu()
        elif employee_option == "2":
            quit()
        else:
            print("You need to choose from options")


class ManagerUI(EmployeeUI):
    """There we are printing all Manager options"""
    def __init__(self, manager):
        super().__init__(manager)

    def show_manager_menu(self):
        """There we are showing Manager menu"""
        print(
            "\n/---------------------"
            "\n| Manager menu:"
            "\n| (1) Show student list"
            "\n| (2) Show mentor list"
            "\n| (3) Edit mentor"
            "\n| (4) Add mentor"
            "\n| (5) Remove mentor"
            "\n| (0) Exit"
            "\n\---------------------"
        )
        mentor_option = input("Choose ur option:")
        if mentor_option == "1":
            self.show_student_list()
        elif mentor_option == "2":
            self.show_mentor_list()
        elif mentor_option == "3":
            self.edit_mentor()
        elif mentor_option == "0":
            quit()
        else:
            print("You need to choose from options: ")

    def show_student_list(self):
        """There we are showing student list"""
        print(Student.student_list_basics())
        employee_table_option = input("\n/---------------------"
                                      "\n| Manager menu:"
                                      "\n| (1) Show student details"
                                      "\n| (2) Return to menu"
                                      "\n| (0) Exit"
                                      "\n\---------------------\n")

        if employee_table_option == "1":
            self.show_student_details()
        elif employee_table_option == "2":
            self.show_manager_menu()
        elif employee_table_option == "0":
            quit()
        else:
            print("You need to choose from option")

    def show_student_details(self):
        """There we are showing student list with details"""
        print(Student.get_student_list())
        print("\n/---------------------"
              "\n| Manager menu:"
              "\n| (1) Return to menu"
              "\n| (0) Exit"
              "\n\---------------------")
        employee_option = input("Choose ur option: ")
        if employee_option == "1":
            self.show_manager_menu()
        elif employee_option == "2":
            quit()
        else:
            print("You need to choose from options")

    def show_mentor_list(self):
        """There we are showing mentor list"""
        Mentor.get_mentor_list()
        print(
            "\n/---------------------"
            "\n| Manager menu:"
            "\n| (1) Show mentor list details"
            "\n| (2) Back to menu"
            "\n| (0) Exit"
            "\n\---------------------"
        )
        mentor_option = input("Choose ur option:")

        if mentor_option == "1":
            self.show_mentor_details_list()
        elif mentor_option == "2":
            self.show_manager_menu()
        elif mentor_option == "0":
            quit()
        else:
            print("You need to choose from options: ")

    @staticmethod
    def edit_mentor():
        Mentor.edit_mentor()

    @staticmethod
    def show_mentor_details_list():
        Mentor.mentor_list_details()

    @staticmethod
    def add_mentor():
        """There we are adding mentor"""
        name = input("Write mentor name: ")
        surname = input("Write mentor surname: ")
        email = input("Write mentor email: ")
        date_of_birth = input("Write mentor date of birth: ")
        city = input("Write mentor city: ")
        phone = input("Write mentor phone: ")
        Mentor(name, surname, email, date_of_birth, city, phone)

    @staticmethod
    def remove_mentor():
        """There we are removing mentor"""
        mentor_id = input("Give mentor ID")
        Mentor.remove_mentor_from_list(mentor_id)


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
                "\n| (4) Check attendance"
                "\n| (5) Edit student"
                "\n| (6) Remove student"
                "\n| (7) Add student"
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
                self.check_attendance()
            elif mentor_option == "5":
                self.edit_student()
            elif mentor_option == "0":
                quit()
            else:
                print("You need to choose from options: ")

    def show_student_list(self):
        """There we are showing student list"""
        print(Student.student_list_basics())
        employee_table_option = input("\n/---------------------"
                                      "\n| Mentor menu:"
                                      "\n| (1) Show student details"
                                      "\n| (2) Return to menu"
                                      "\n| (0) Exit"
                                      "\n\---------------------\n")

        if employee_table_option == "1":
            self.show_student_details()
        elif employee_table_option == "2":
            self.show_mentor_menu()
        elif employee_table_option == "0":
            quit()
        else:
            print("You need to choose from option")

    def show_student_details(self):
        """There we are showing student list with details"""
        print(Student.get_student_list())
        print("\n/---------------------"
              "\n| Mentor menu:"
              "\n| (1) Return to menu"
              "\n| (0) Exit"
              "\n\---------------------")
        employee_option = input("Choose ur option: ")
        if employee_option == "1":
            self.show_mentor_menu()
        elif employee_option == "2":
            quit()
        else:
            print("You need to choose from options")

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
        assigment.get_student_solution_link(student_id)
        new_grade = input("Write new rate for student")
        assigment.grade_student_assigment(student_id, new_grade)

    @staticmethod
    def check_attendance():
        """There we are checking student attendance"""
        student_id = input("Write student id")
        Attendance.check_attendance(student_id)

    @staticmethod
    def edit_student():
        Student.edit_student()

    @staticmethod
    def add_student():
        """There we are adding student to codecool"""
        name = input("Write student name: ")
        surname = input("Write student surname: ")
        email = input("Write student email: ")
        date_of_birth = input("Write student date of birth: ")
        city = input("Write student city: ")
        phone = input("Write student phone: ")
        Student(name, surname, email, date_of_birth, city, phone, attendance_level=0)

    @staticmethod
    def remove_student():
        """There we are removing student by his id"""
        student_id = input("Write me student id")
        Student.remove_student_from_list(student_id)
