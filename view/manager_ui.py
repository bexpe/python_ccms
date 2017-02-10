from controller.student_ctrl import Student
from controller.mentor_ctrl import Mentor
from view.employee_ui import EmployeeUI
from terminaltables import AsciiTable 


class ManagerUI(EmployeeUI):
    """There we are printing all Manager options"""

    def __init__(self, manager):
        super().__init__(manager)

    def show_manager_menu(self):
        """There we are showing Manager menu"""
        while True:
            print(
                "\n/---------------------"
                "\n| Manager menu:"
                "\n| (1) Show student list"
                "\n| (2) Show student details"
                "\n| (3) Show mentor list"
                "\n| (4) Show mentor details"
                "\n| (5) Edit mentor"   #BUGS
                "\n| (6) Add mentor"    #BUGS
                "\n| (7) Remove mentor" #BUGS
                "\n| (8) Show full statistics of mentors and students"  #BUGS
                "\n| (9) Show each student average grade"   #TODO
                "\n| (0) Exit"
                "\n\---------------------"
            )
            manager_option = input("| Choose your option: ")
            if manager_option == "1":
                self.show_student_list()
            if manager_option == "2":
                self.show_student_details()
            elif manager_option == "3":
                self.show_mentor_list()
            elif manager_option == "4":
                self.show_mentor_details()
            elif manager_option == "5":
                self.edit_mentor()
            elif manager_option == "6":
                self.add_mentor()
            elif manager_option == "7":
                self.remove_mentor()
            elif manager_option == "8":
                self.show_full_statistics_of_mentors_and_students()
            elif manager_option == "9":
                self.show_each_student_average_grade()
            elif manager_option == "0":
                break
            else:
                print("You need to choose from options: ")

    def show_mentor_list(self):
        mentor_list = Mentor.get_mentors_list()
        table_head = ['Name', 'Surname', 'Email']
        table_basic = [[d[1],d[2],d[3]] for d in mentor_list]
        table_basic.insert(0, table_head)
        table = AsciiTable(table_basic)
        print("\n" + table.table)
        input(" *** Click enter to continue *** ")

    @staticmethod
    def show_mentor_details():
        print(
            "\n/---------------------"
            "\n| Show mentor details:"
        )
        mentor_name = input("| Insert mentor name: ")
        mentor_surname = input("| Insert mentor surname: ")
        mentor_details = Mentor.get_mentor_details(mentor_name, mentor_surname)
        if mentor_details:
            mentor_details = mentor_details[0]
            print((
            "\n/---------------------"
            "\n| {} {} details:"
            "\n| Email: {}"
            "\n| Date of birth: {}"
            "\n| City: {}"
            "\n| Phone: {}"
            "\n\---------------------"
        ).format(
                mentor_details[0],
                mentor_details[1],
                mentor_details[2],
                mentor_details[3],
                mentor_details[4],
                mentor_details[5],
                )
        )
        else:
            print(" *** Mentor not found *** ")

    @staticmethod
    def edit_mentor():
        print(
            "\n/---------------------"
            "\n| Edit mentor"
        )
        cur_name = input("| Write mentor name: ")
        cur_surname = input("| Write mentor surname: ")
        mentor = mentor.get_student_details(cur_name, cur_surname)
        if mentor:
            name = input("| Write mentor name: ")
            surname = input("| Write mentor surname: ")
            email = input("| Write mentor email: ")
            date_of_birth = input("| Write mentor date of birth: ")
            city = input("| Write mentor city: ")
            phone = input("| Write mentor phone: ")
            Mentor.edit_mentor(cur_name, cur_surname, name, surname, email, date_of_birth, city, phone)
            print(" *** Mentor edited *** ")
        else:
            print(" *** Mentor not found *** ")

    @staticmethod
    def add_mentor():
        """There we are adding mentor"""
        print(
            "\n/---------------------"
            "\n| Add mentor:"
        )
        name = input("| Write mentor name: ")
        surname = input("| Write mentor surname: ")
        email = input("| Write mentor email: ")
        date_of_birth = input("| Write mentor date of birth: ")
        city = input("| Write mentor city: ")
        phone = input("| Write mentor phone: ")
        Mentor.add_new_mentor(name, surname, email, date_of_birth, city, phone)

    @staticmethod
    def remove_mentor():
        print(
            "\n/---------------------"
            "\n| Remove mentor "
        )
        name = input("| Write mentor name: ")
        surname = input("| Write mentor surname: ")
        mentor = Mentor.get_mentor_details(name, surname)
        if mentor:
            Mentor.remove_mentor_from_data_base(name, surname)
        else:
            print(" *** Mentor not found *** ")

    def show_full_statistics_of_mentors_and_students(self):
        print((
            "\n/---------------------"
            "\n| Statistics:"
            "{}"
            "\n\---------------------"
        ).format(
            ''.join(self.student.get_student_overall_attendance()) # nowa metoda |
        ))

    def show_each_student_average_grade(self):
        print((
            "\n/---------------------"
            "\n| Average grade:"
            "{}"
            "\n\---------------------"
        ).format(
            ''.join(self.student.get_student_overall_attendance()) # nowa metoda |
        ))
