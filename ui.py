class StudentUI():
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
            self.show_student_list()
        elif employee_options == "0":
            quit()
        else:
            print("You need to choose from options")

    def show_student_list(self):
        # Student.table



class ManagerUI(EmployeeUI):
    pass


class MentorUI(EmployeeUI):

    def __init__(self, mentor):
        self.mentor = mentor

    def menotr_menu(self):
        print(
            "\n/---------------------"
            "\n| Mentor menu:"
            "\n| (1) Show student list"
            "\n| (2) Show student list"
            "\n| (1) Show student list"
            "\n| (1) Show student list"
            "\n| (1) Show student list"
            "\n| (1) Show student list"
            "\n| (0) Exit"
            "\n\---------------------"
        )