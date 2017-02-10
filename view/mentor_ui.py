from controller.student_ctrl import Student
from view.employee_ui import EmployeeUI
from controller.attendance_ctrl import Attendance
import datetime
from model.group_team_model import Team


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
                #"\n| (3) Add assignment"
                #"\n| (4) Grade assignment"
                #"\n| (5) Check attendance"
                "\n| (6) Edit student"
                "\n| (7) Remove student"
                "\n| (8) Add student"
                "\n| (9) Create student team"
                #"\n| (10) Add student to team"
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
                #self.add_assignment()
                pass
            elif mentor_option == "4":
                #self.grade_assignment()
                pass
            elif mentor_option == "5":
                #self.check_attendance()
                pass
            elif mentor_option == "6":
                self.edit_student()
            elif mentor_option == "7":
                self.remove_student()
            elif mentor_option == "8":
                self.add_student()
            elif mentor_option == "9":
                self.create_student_team()
            elif mentor_option == "10":
                #self.add_student_to_team()
                pass
            elif mentor_option == "11":
                self.list_students_groups()
            elif mentor_option == "12":
                self.add_cards_to_students()
            elif mentor_option == "0":
                break
            else:
                print("Bad choice. Enter correct value.")

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
        ).format(datetime.datetime.now().date())
        )
        while True:
            student_id = input('Insert student id: ')
            student = Student.check_student_in_db_by_id(student_id)
            print(student)
            if not student:
                print('Invalid id')
                continue
            date = datetime.datetime.now().date()
            option = input('p = present, l = late a = absent: ')
            option = option.upper()
            if option == 'P':
                attendance = 'present'
            elif option == 'L':
                attendance = 'late'
            elif option == 'A':
                attendance = 'absent'
            else:
                print("There is no such option.")
                continue

            if option in ('P', 'L', 'A'):
                Attendance.set_attendance(student_id, date, attendance)
            else:
                print(" *** Bad input *** ")
                continue

    @staticmethod
    def edit_student():
        print(
            "\n/---------------------"
            "\n| Edit student"
        )
        cur_name = input("| Write student name: ")
        cur_surname = input("| Write student surname: ")
        student = Student.get_student_details(cur_name, cur_surname)
        if student:
            name = input("| Write student name: ")
            surname = input("| Write student surname: ")
            email = input("| Write student email: ")
            date_of_birth = input("| Write student date of birth: ")
            city = input("| Write student city: ")
            phone = input("| Write student phone: ")
            Student.edit_student(cur_name, cur_surname, name, surname, email, date_of_birth, city, phone)
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
        Student.add_student(name, surname, email, date_of_birth, city, phone)
        print("*** Student added ***")

    @staticmethod
    def remove_student():
        """There we are removing student by his id"""
        print(
            "\n/---------------------"
            "\n| Remove student"
        )
        name = input("| Write student name: ")
        surname = input("| Write student surname: ")
        student = Student.get_student_details(name, surname)
        if student:
            Student.remove_student_from_data_base(name, surname)
            print(" *** Student removed *** ")
        else:
            print(" *** Student not found *** ")

    @staticmethod
    def create_student_team():
        team = Team()

        print(
            "\n/---------------------"
            "\n| Create new team"
        )
        new_team_name = input("| Insert team name: ")
        assignment_id = input(" Please insert id for an assignment for this team ")
        team.create_team(new_team_name, assignment_id)
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
        team_model = Team()
        print(
            "\n/---------------------"
            "\n| Students groups"
        )
        for group in team_model.display_all_groups():
            print("| Group name: {}".format(group[1]))

    @staticmethod
    def add_cards_to_students():
        print(
            "\n/---------------------"
            "\n| Add cards to team"
        )
        name = input("| Write student name: ")
        surname = input("| Write student surname: ")
        student = Student.get_student_details(name, surname)
        if student:
            while True:
                card_to_add = input("| Which card you want add? [r-red, y-yellow, g-green]: ")
                if card_to_add in ('r', 'y', 'g'):
                    Student.add_card(card_to_add, name, surname)
                    print(" *** Student card added *** ")
                    break
                else:
                    print(" *** Bad card number *** ")
        else:
            print(" *** Student not found *** ")
