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
                break
            else:
                print("You need to choose from options")

    def show_student_list(self):
        """There we are showing student list"""
        print(Student.student_list_basics())
        while True:
            employee_table_option = input("\n/---------------------"
                                          "\n| Student list:"
                                          "\n| (1) Show student details"
                                          "\n| (2) Return to menu"
                                          "\n\---------------------\n")

            if employee_table_option == "1":
                print(Student.get_student_list())
            elif employee_table_option == "2":
                break
            else:
                print("You need to choose from option")