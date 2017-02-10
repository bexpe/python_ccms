from model.mentor_model import Mentor_model
from controller.employee_ctrl import Employee

class Mentor(Employee):

    def __init__(self, name, surname, email, date_of_birth, city, phone):
        super().__init__(name, surname, email, date_of_birth, city, phone)

    def get_mentor_details(self):
        return self.get_details_basic()

    def remove_mentor(self):
        Mentor_model.remove_mentor(self.get_full_name())

    @staticmethod
    def get_mentors_list():
        model = Mentor_model()
        list_of_mentors = model.get_list_of_mentors()
        return list_of_mentors

    @staticmethod
    def add_new_mentor(name, surname, email, date_of_birth, city, phone):
        Mentor.add_new_mentor(name, surname, email, date_of_birth, city, phone)