class StudentUI():

    def __init__(self, student):
        self.student = student

    def show_student_menu(self):
        while True:
            print(
                "\n/---------------------"
                "\n| Student menu:"
                "\n| (1) Show my grades"
                "\n| (2) Show assigments"
                "\n| (3) Submit assigment"
                "\n| (0) Exit"
                "\n\---------------------"
            )
            user_choose = input('Your choose: ')
            if user_choose == "1":
                self.show_student_grade_ui():
            elif user_choose == "2":
                self.show_assigments_ui():
            elif user_choose == "3":
                self.submit_assigment_ui():
            elif user_choose == "0":
                quit()
            else:
                print("Bad choice. Enter correct value.")

    def show_student_grade_ui(self):
        pass

    def show_assigments_ui(self):
        pass

    def submit_assigment_ui(self):
        pass


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
            # Student.table
        elif employee_options == "0":
            quit()
        else:
            print("You need to choose from options")


class ManagerUI(EmployeeUI):
    pass


class MentorUI(EmployeeUI):
    pass
