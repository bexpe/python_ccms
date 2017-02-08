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
            elif mentor_option == "4":
                self.add_mentor()
            elif mentor_option == "5":
                self.remove_mentor()
            elif mentor_option == "0":
                break
            else:
                print("You need to choose from options: ")

    def show_mentor_list(self):
        """There we are showing mentor list"""
        print(Mentor.mentor_list_basics())
        while True:
            print(
                "\n/---------------------"
                "\n| Manager menu:"
                "\n| (1) Show mentor list details"
                "\n| (2) Back to menu"
                "\n\---------------------"
            )
            mentor_option = input("Choose ur option:")

            if mentor_option == "1":
                print(Mentor.get_mentor_list())
            elif mentor_option == "2":
                break
            else:
                print("You need to choose from options: ")

    @staticmethod
    def edit_mentor():
        print(Mentor.get_mentor_list())
        mentor_id = input("Insert mentor id: ")
        mentor = Mentor.get_mentor_from_list_by_id(mentor_id)
        if mentor:
            mentor.edit_user()
            print("*** Mentor edited ***")
        else:
            print("*** Mentor not found ***")

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
        new_mentor = Mentor(name, surname, email, date_of_birth, city, phone)

    @staticmethod
    def remove_mentor():
        """There we are removing mentor"""
        mentor_id = input("Give mentor ID: ")
        Mentor.remove_mentor_from_list(mentor_id)