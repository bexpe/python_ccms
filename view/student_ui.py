from controller.student_ctrl import Student
#from controller.assigment_ctrl import Assigment


class StudentUI():

    def __init__(self, student):
        self.student = student

    def show_student_menu(self):
        while True:
            print(
                "\n/---------------------"
                "\n| Student menu:"
                "\n| (1) Show my grades"
                "\n| (2) See my overall attendance"
                "\n| (3) Submit assignment"
                "\n| (4) Submit team assigment"
                "\n| (0) Exit"
                "\n\---------------------"
            )
            user_choose = input('Your choose: ')
            if user_choose == "1":
                self.show_student_grade_ui()
            elif user_choose == "2":
                self.show_student_overall_attendance_ui()
            elif user_choose == "3":
                self.submit_assigment_ui()
            elif user_choose == "4":
                self.submit_assigment_as_team_ui()
            elif user_choose == "0":
                break
            else:
                print("Bad choice. Enter correct value.")

    def show_student_grade_ui(self):
        student_grades = self.student.get_student_grades()
        student_grades_table = ["\n| {} : {} %".format(task_name, grade) for task_name, grade in student_grades.items()]
        print((
            "\n/---------------------"
            "\n| Your grades:"
            "{}"
            "\n\---------------------"
        ).format(
            ''.join(student_grades_table)
        ))

    def show_student_overall_attendance_ui(self):
        print((
            "\n/---------------------"
            "\n| Your overall attendance:"
            "{}"
            "\n\---------------------"
        ).format(
            ''.join(self.student.get_student_overall_attendance()) # nowa metoda |
        ))

    def submit_assigment_ui(self):
        assigments_list = Assigment.get_assigments_list()
        assigments_table = ["\n| {}".format(assigment_name) for assigment_name in assigments_list]
        print((
            "\n/---------------------"
            "\n| Assigments:"
            "{}"
            "\n|---------------------"
            "\n| Submit assigment"
            "\n|"
        ).format(
            ''.join(assigments_table)
        ))
        # to poniżej do przemyślenia ( controler )
        assigment_name = input('| Assigment name: ')
        assigment = Assigment.get_assigment_by_name(assigment_name)  # do poprawy? crash?
        if assigment:
            student_solution = input('| Insert your solution(github link): ')
            assigment.submit_assigment_answer(self.student.get_student_id(), student_solution)
            print(" *** Solution added *** ")
        else:
            print(" *** Assigment not found *** ")

    def submit_assigment_as_team_ui(self):
        assigments_list = Assigment.get_team_assigments_list() # dodana metoda get_team_assigments
        # TODO
        # to poniżej ma być w kontrolerze
        assigments_table = ["\n| {}".format(assigment.get_assigment_name()) for assigment in assigments_list]
        # end todo
        print((
            "\n/---------------------"
            "\n| Assigments:"
            "{}"
            "\n|---------------------"
            "\n| Submit assigment"
            "\n|"
        ).format(
            ''.join(assigments_table)
        ))
        # to poniżej do przemyślenia ( controler )
        assigment_name = input('| Assigment name: ')
        assigment = Assigment.get_team_assigment_by_name(assigment_name)  # do poprawy? crash?
        if assigment:
            student_solution = input('| Insert your team solution(github link): ')
            assigment.submit_assigment_answer(self.student.get_student_team_id(), student_solution) # dodana metoda
            print(" *** Team solution added *** ")
        else:
            print(" *** Assigment not found *** ")
