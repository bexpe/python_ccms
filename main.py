"""
LOGINS TO SYSTEM
usertype:   email:      password
mentor :    mentor@cc   memen
student:    student@cc  ststu
manager:    jurek@cc    jujer
employee:   emp@cc      ememp

O
"""

from ui import *
from users import *
from assigments import Assigment
import getpass


class Main:
    def __init__(self):
        self.load_list()
        self.sign_in()
        self.save_list()

    def __init__(self):
        self.load_list()
        self.sign_in()
        self.save_list()

    def load_list(self):
        Student.load_students_csv()
        Employee.load_employees_csv()
        Mentor.load_mentor_csv()
        Manager.load_manager_csv()
        Assigment.load_assigment_csv()

    def save_list(self):
        Student.save_students_csv()
        Employee.save_employees_csv()
        Mentor.save_mentor_csv()
        Manager.save_manager_csv()
        Assigment.save_assigment_csv()

    def sign_in(self):
        user_email = input("Input your email: ")
        user_password = getpass.getpass("Input your password: ")
        hash_password = hashlib.md5(user_password.encode())
        user_password = hash_password.hexdigest()

        for student in Student.get_students_objects():
            if student.get_email() == user_email:
                if student.get_password() == user_password:
                    student_UI = StudentUI(student)
                    student_UI.show_student_menu()
                    return

        for mentor in Mentor.get_mentors_objects():
            if mentor.get_email() == user_email:
                if mentor.get_password() == user_password:
                    mentor_UI = MentorUI(mentor)
                    mentor_UI.show_mentor_menu()
                    return

        for employee in Employee.get_employees_objects():
            if employee.get_email() == user_email:
                if employee.get_password() == user_password:
                    employee_UI = EmployeeUI(employee)
                    employee_UI.show_employee_menu()
                    return

        for manager in Manager.get_managers_objects():
            if manager.get_email() == user_email:
                if manager.get_password() == user_password:
                    manager_UI = ManagerUI(manager)
                    manager_UI.show_manager_menu()
                    return

    def load_list(self):
        Student.load_students_csv()
        Employee.load_employees_csv()
        Mentor.load_mentor_csv()
        Manager.load_manager_csv()
        Assigment.load_assigment_csv()
        Attendance.load_students_attendance_()

    def save_list(self):
        Student.save_students_csv()
        Employee.save_employees_csv()
        Mentor.save_mentor_csv()
        Manager.save_manager_csv()
        Assigment.save_assigment_csv()

    def sign_in(self):
        user_email = input("Input your email: ")
        user_password = getpass.getpass("Input your password: ")
        hash_password = hashlib.md5(user_password.encode())
        user_password = hash_password.hexdigest()

        for student in Student.get_students_objects():
            if student.get_email() == user_email:
                if student.get_password() == user_password:
                    student_UI = StudentUI(student)
                    student_UI.show_student_menu()
                    return

        for mentor in Mentor.get_mentors_objects():
            if mentor.get_email() == user_email:
                if mentor.get_password() == user_password:
                    mentor_UI = MentorUI(mentor)
                    mentor_UI.show_mentor_menu()
                    return

        for employee in Employee.get_employees_objects():
            if employee.get_email() == user_email:
                if employee.get_password() == user_password:
                    employee_UI = EmployeeUI(employee)
                    employee_UI.show_employee_menu()
                    return

        for manager in Manager.get_managers_objects():
            if manager.get_email() == user_email:
                if manager.get_password() == user_password:
                    manager_UI = ManagerUI(manager)
                    manager_UI.show_manager_menu()
                    return

if __name__ == "__main__":
    main = Main()
