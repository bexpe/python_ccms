from assigments import Assigments


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
        student_grades = self.student.get_student_grades()
        student_grades_table = ["| {} : {} %".format(key, value) for key, value in student_grades.items()]

        print((
            "\n/---------------------"
            "\n| Your grades:"
            "{}"
            "\n\---------------------"
        ).format(
            ''.join(student_grades_table)
        ))

    def show_assigments_ui(self):
        assigments = Assigments.get_assigments_list()
        assigments_table = ["| {}".format(assigment.get_assigment_name()) for assigment in assigments]

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
        assigment = Assigment.get_assigment_by_name(assigment_name)
        if assigment:
            student_solution = input('| Insert your solution(github link): ')
            assigment.submit_assigment_answer(self.student.get_student_id(), student_solution)
            print(" *** Solution added *** ")
        else:
            print(" *** Assigment not found *** ")



class EmployeeUI:

    def __init__(self, employee):
        self.employee = employee

    def employee_menu(self):
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
        # Student.table
        print("\n/---------------------"
              "\n| Employee menu:"
              "\n| (1) Show student details"
              "\n| (2) Return to menu"
              "\n| (0) Exit"
              "\n\---------------------")
        employee_table_option = input("Choose option")
        if employee_table_option == "1":
            self.employee_menu()
        elif employee_table_option == "2":
            pass
        elif employee_table_option == "0":
            quit()
        else:
            print("You need to choose from option")


class ManagerUI(EmployeeUI):
    pass


class MentorUI(EmployeeUI):

    def __init__(self, mentor):
        super().__init__(mentor)

    def mentor_menu(self):

        print(
            "\n/---------------------"
            "\n| Mentor menu:"
            "\n| (1) Show student list"
            "\n| (2) Add assignment"
            "\n| (3) Grade assignment"
            "\n| (4) Check attendance"
            "\n| (5) Edit student"
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

    def add_assignment(self):
        pass

    def grade_assignment(self):
        pass

    def check_attendance(self):
        pass

    def edit_student(self):
        pass
