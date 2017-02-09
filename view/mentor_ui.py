from control.student_ctrl import Student
import datetime


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
                "\n| (2) Show student details"
                "\n| (3) Add assignment"
                "\n| (4) Grade assignment"
                "\n| (5) Check attendance"
                "\n| (6) Edit student"
                "\n| (7) Remove student"
                "\n| (8) Add student"
                "\n| (9) Create student team"
                "\n| (10) Add student to team"
                "\n| (11) List student teams"
                "\n| (12) Add card to student"
                "\n| (0) Exit"
                "\n\---------------------"
            )
            mentor_option = input("| Choose your option:")
            if mentor_option == "1":
                self.show_student_list()
            if mentor_option == "2":
                self.show_student_details()
            elif mentor_option == "3":
                self.add_assignment()
            elif mentor_option == "4":
                self.grade_assignment()
            elif mentor_option == "5":
                self.check_attendance()
            elif mentor_option == "6":
                self.edit_student()
            elif mentor_option == "7":
                self.remove_student()
            elif mentor_option == "8":
                self.add_student()
            elif mentor_option == "9":
                self.create_student_team()
            elif mentor_option == "10":
                self.add_student_to_team()
            elif mentor_option == "11":
                self.list_students_groups()
            elif mentor_option == "12":
                self.add_cards_to_students()
            elif mentor_option == "0":
                break
            else:
                print("You need to choose from options: ")

    @staticmethod
    def add_assignment():
        """There we are adding assignment"""
        print(
            "\n/---------------------"
            "\n| Add new assigment"
        )
        assigment_name = input("| Write name for new assigment: ")
        description = input("| Write description for new assignment: ")
        Assigment(assigment_name, description)

    @staticmethod
    def grade_assignment():
        """There we are grade assignment"""
        print(
            "\n/---------------------"
            "\n| Grading assigment"
        )
        assignment_to_find = input("| Write assignment name that you want to grade: ")
        assigment = Assigment.get_assigment_by_name(assignment_to_find)
        if assigment:
            student_name = input("| Write student full name: ")
            student = Student.get_student_by_name(student_name)
            if student:
                student_id = student.get_student_id()
                print("| Student answer: ", assigment.get_student_solution_link(student_id))
                new_grade = input("| New rate for student: ")
                # if mentor input sometihing another than numbers, integers?
                assigment.grade_student_answer(student_id, new_grade)
            else:
                print(" *** Student not found *** ")
        else:
            print(" *** Assigment not found *** ")

    @staticmethod
    def check_attendance():
        """Print students list and particular student attendance"""
        print((
            "\n/---------------------"
            "\n| Checking attendance for {}"
            "\n| p - present, l - late, a - absent"
        ).format(datetime.datetime.now())
        )
        for student in Student.get_student_list():
            while True:
                student_status = input("| {}: ".format(student.get_student_full_name()))
                if student_status in ('p', 'l', 'a'):
                    student.set_student_attendance(student_status)
                else:
                    print(" *** Bad input *** ")

    @staticmethod
    def edit_student():
        print(
            "\n/---------------------"
            "\n| Edit student"
        )
        student_name = input("| Write student full name: ")
        student = Student.get_student_by_name(student_name)
        if student:
            name = input("| Write student name: ")
            surname = input("| Write student surname: ")
            email = input("| Write student email: ")
            date_of_birth = input("| Write student date of birth: ")
            city = input("| Write student city: ")
            phone = input("| Write student phone: ")
            student.edit_user(name, surname, email, date_of_birth, city, phone)
            print("*** Student edited ***")
        else:
            print("*** Student not found ***")

    @staticmethod
    def add_student():
        """There we are adding student to codecool"""
        print(
            "\n/---------------------"
            "\n| Add student"
        )
        name = input("| Write student name: ")
        surname = input("| Write student surname: ")
        email = input("| Write student email: ")
        date_of_birth = input("| Write student date of birth: ")
        city = input("| Write student city: ")
        phone = input("| Write student phone: ")
        student.add_new_student(name, surname, email, date_of_birth, city, phone)
        print("*** Student added ***")

    @staticmethod
    def remove_student():
        """There we are removing student by his id"""
        print(
            "\n/---------------------"
            "\n| Add student"
        )
        student_name = input("| Write student full name: ")
        student = Student.get_student_by_name(student_name)
        if student:
            student.remove_student()
        else:
            print(" *** Student not found *** ")

    @staticmethod
    def create_student_team():
        print(
            "\n/---------------------"
            "\n| Create new team"
        )
        new_team_name = input("| Insert team name: ")
        Mentor.create_student_team(new_team_name)
        print(" *** Team created *** ")

    @staticmethod
    def add_student_to_team():
        print(
            "\n/---------------------"
            "\n| Add student to team"
        )
        team_name = input("| Insert team name: ")
        team = Mentor.get_team_by_name(team_name)
        if team:
            student_name = input("| Write student full name to add: ")
            student = Student.get_student_by_name(student_name)
            if student:
                team.add_student_to_team(student)
                print(" *** Student added to team *** ")
            else:
                print(" *** Student not found *** ")
        else:
            print(" *** Team not found *** ")

    @staticmethod
    def list_students_groups():
        print(
            "\n/---------------------"
            "\n| Students groups"
        )
        for group in Mentor.get_list_of_teams():
            print("| Group: {}".format(group))

    @staticmethod
    def add_cards_to_students():
        print(
            "\n/---------------------"
            "\n| Add cards to team"
        )
        student_name = input("| Write student full name to add: ")
        student = Student.get_student_by_name(student_name)
        if student:
            while True:
                card_to_add = input("| Which card you want add? r-red, y-yellow, g-green]: ")
                if card_to_add in ('r', 'y', 'g'):
                    student.add_card(card_to_add)
                    print(" *** Student card added *** ")
                    break
                else:
                    print(" *** Bad card number *** ")
        else:
            print(" *** Student not found *** ")
