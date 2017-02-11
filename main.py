"""
LOGINS TO SYSTEM
usertype:   email:      password
mentor :    mentor@m      dupa
student:    marek@s       dupa
manager:    jurek@j       dupa
employee:   miriam@e      dupa
"""

from view.student_ui import StudentUI
from view.mentor_ui import MentorUI
from view.employee_ui import EmployeeUI
from view.manager_ui import ManagerUI
from controller.student_ctrl import Student
from controller.mentor_ctrl import Mentor
from controller.employee_ctrl import Employee
from controller.manager_ctrl import Manager
import model.open_database
import getpass
import hashlib


def sign_in():
    print(
        "\n/---------------------"
        "\n| Welcome in Canvas system:"
        "\n| "
    )
    while True:
        user_login = input("| Input your login: ")
        user_password = getpass.getpass("| Input your password: ")
        #hash_password = hashlib.md5(user_password.encode())
        #user_password = hash_password.hexdigest()
        for s_data in Student.get_students_list():
            if s_data[8] == user_login:
                if s_data[9] == user_password:
                    print(
                        "| Succesfull login"
                        "\n\---------------------"
                    )
                    student_object = Student(s_data[1], s_data[2], s_data[3], s_data[4], s_data[5], s_data[6], s_data[7], s_data[10], s_data[11])
                    student_UI = StudentUI(student_object)
                    student_UI.show_student_menu()
                    return
        for m_data in Mentor.get_mentors_list():
            if m_data[7] == user_login:
                if m_data[8] == user_password:
                    print(
                        "| Succesfull login"
                        "\n\---------------------"
                    )
                    mentor_object = Mentor(m_data[1], m_data[2], m_data[3], m_data[4], m_data[5], m_data[6])
                    mentor_UI = MentorUI(mentor_object)
                    mentor_UI.show_mentor_menu()
                    return
        for e_data in Employee.get_employees_list():
            if e_data[7] == user_login:
                if e_data[8] == user_password:
                    print(
                        "| Succesfull login"
                        "\n\---------------------"
                    )
                    employee_object = Employee(e_data[1], e_data[2], e_data[3], e_data[4], e_data[5], e_data[6])
                    employee_UI = EmployeeUI(employee_object)
                    employee_UI.show_employee_menu()
                    return
        for j_data in Manager.get_managers_list():
            if j_data[7] == user_login:
                if j_data[8] == user_password:
                    print(
                        "| Succesfull login"
                        "\n\---------------------"
                    )
                    manager_object = Manager(j_data[1], j_data[2], j_data[3], j_data[4], j_data[5], j_data[6])
                    manager_UI = ManagerUI(manager_object)
                    manager_UI.show_manager_menu()
                    return
        print(
            "| Bad login or password. Try again."
        )

if __name__ == "__main__":
    model.open_database.load_database()
    sign_in()
