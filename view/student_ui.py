from assigments import Assigment
from attendance import Attendance


class StudentUI():
    def __init__(self, student):
        self.student = student

    def show_student_menu(self):
        while True:
            print(
                "\n/---------------------"
                "\n| Student menu:"
                "\n| (1) Show my grades"
                "\n| (2) Show assignments"
                "\n| (3) Submit assignment"
                "\n| (0) Exit"
                "\n\---------------------"
            )
            user_choose = input('Your choose: ')
            if user_choose == "1":
                self.show_student_grade_ui()
            elif user_choose == "2":
                self.show_assigments_ui()
            elif user_choose == "3":
                self.submit_assigment_ui()
            elif user_choose == "0":
                break
            else:
                print("Bad choice. Enter correct value.")

    def show_student_grade_ui(self):
        student_grades = {}

        assigments_list = Assigment.get_assigments_list()
        for assigment in assigments_list:
            grade = assigment.get_student_grade(self.student.get_student_id())
            student_grades[assigment.get_assigment_name()] = grade

        student_grades_table = ["\n| {} : {} %".format(key, value) for key, value in student_grades.items()]

        print((
            "\n/---------------------"
            "\n| Your grades:"
            "{}"
            "\n\---------------------"
        ).format(
            ''.join(student_grades_table)
        ))

    @staticmethod
    def show_assigments_ui():
        assigments_list = Assigment.get_assigments_list()
        assigments_table = ["\n| {}".format(assigment.get_assigment_name()) for assigment in assigments_list]

        print((
            "\n/---------------------"
            "\n| Assigments:"
            "{}"
            "\n\---------------------"
        ).format(
            ''.join(assigments_table)
        ))

    def submit_assigment_ui(self):
        print(
            "\n/---------------------"
            "\n| Submit assigment"
            "\n|"
        )
        assigment_name = input('| Assigment name: ')
        assigment = Assigment.get_assigment_by_name(assigment_name)  # do poprawy
        if assigment:
            student_solution = input('| Insert your solution(github link): ')
            assigment.submit_assigment_answer(self.student.get_student_id(), student_solution)
            print(" *** Solution added *** ")
        else:
            print(" *** Assigment not found *** ")