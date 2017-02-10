from controller.student_ctrl import Student
from terminaltables import AsciiTable 
# pip3 install terminaltables


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
        table_head = ['Name', 'Surname', 'Email']
        table_basic = [[d[1],d[2],d[3]] for d in student_list]
        table_basic.insert(0, table_head)
        table = AsciiTable(table_basic)
        print("\n" + table.table)
        input(" *** Click enter to continue *** ")

    def show_student_details(self):
        """There we are showing student list"""
        print(
            "\n/---------------------"
            "\n| Show student details"
        )
        student_name = input("| Insert student name: ")
        student_surname = input("| Insert student surname: ")
        student_details = Student.get_student_details(student_name, student_surname)
        if student_details:
            student_details = student_details[0]
            print((
            "\n/---------------------"
            "\n| {} {} details:"
            "\n| Email: {}"
            "\n| Date of birth: {}"
            "\n| City: {}"
            "\n| Phone: {}"
            "\n| Attendance: {}"
            "\n| Card: {}"
            "\n\---------------------"
        ).format(
                student_details[0],
                student_details[1],
                student_details[2],
                student_details[3],
                student_details[4],
                student_details[5],
                student_details[6],
                student_details[7]
                )
        )
        else:
            print(" *** Student not found *** ")
