from control.student_ctrl import Student


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
                "\n| (1) Show students list"
                "\n| (2) Show student details"
                "\n| (0) Exit"
                "\n\---------------------"
            )
            employee_options = input("| Choose your option: ")
            if employee_options == "1":
                self.show_student_list()
            elif employee_options == "2":
                self.show_student_details()
            elif employee_options == "0":
                break
            else:
                print("Bad choice. Enter correct value.")

    def show_student_list(self):
        student_list = Student.get_students_list()
        # pretty table?

    def show_student_details(self):
        """There we are showing student list"""
        print(
            "\n/---------------------"
            "\n| Insert student name and surname to show informations:"
        )
        student_name = input("| ")
        student = Student.get_student_by_name(student_name)  # new method
        if student:
            print(student.get_student_details(student_name))  # new method
        else:
            print(" *** Student not found *** ")
