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
                "\n| (5) Edit mentor"
                "\n| (6) Add mentor"
                "\n| (7) Remove mentor"
                "\n| (8) Show full statistics of mentors and students"
                "\n| (9) Show each student average grade"
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
        mentor_list = Mentor.get_mentor_list()
        # pretty table?

    @staticmethod
    def show_mentor_details_list():
        print(
            "\n/---------------------"
            "\n| Insert mentor name and surname to show informations:"
        )
        mentor_name = input("| ")
        mentor = Mentor.get_mentor_by_name(mentor_name)  # new method
        if mentor:
            print(mentor.get_mentor_details(mentor_name))  # new method
        else:
            print(" *** Mentor not found *** ")

    @staticmethod
    def edit_mentor():
        print(
            "\n/---------------------"
            "\n| Edit mentor"
        )
        mentor_name = input("| Insert mentor name and surname to edit:")
        mentor = Mentor.get_mentor_by_name(mentor_name)  # new method
        if mentor:
            name = input("| Write mentor name: ")
            surname = input("| Write mentor surname: ")
            email = input("| Write mentor email: ")
            date_of_birth = input("| Write mentor date of birth: ")
            city = input("| Write mentor city: ")
            phone = input("| Write mentor phone: ")
            mentor.edit_user(name, surname, email, date_of_birth, city, phone)
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
        mentor_name = input("| Insert mentor name and surname to remove: ")
        mentor = Mentor.get_mentor_by_name(mentor_name)  # new method
        if mentor:
            mentor.remove_mentor()
            print(" *** Mentor removed *** ")
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
