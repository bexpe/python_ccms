from model.mentor_model import Mentor_model
from controller.employee_ctrl import Employee

class Mentor(Employee):

    def __init__(self, name, surname, email, date_of_birth, city, phone):
        super().__init__(name, surname, email, date_of_birth, city, phone)

    @staticmethod
    def get_mentors_list():
        model = Mentor_model()
        list_of_mentors = model.get_list_of_mentors()
        return list_of_mentors

    @staticmethod
    def add_new_mentor(name, surname, email, date_of_birth, city, phone):
        model = Mentor_model()
        model.add_mentor(name, surname, email, date_of_birth, city, phone)

    @staticmethod
    def get_mentor_details(mentor_name, mentor_surname):
        model = Mentor_model()
        mentor_details = model.get_mentor_detail(mentor_name, mentor_surname)
        return mentor_details

    @staticmethod
    def edit_mentor(cur_name, cur_surname, name, surname, email, date_of_birth, city, phone):
        model = Mentor_model()
        model.edit_mentor(cur_name, cur_surname, name, surname, email, date_of_birth, city, phone)

    @staticmethod
    def remove_mentor_from_data_base(mentor_name, mentor_surname):
        model = Mentor_model()
        model.remove_mentor_from_database(mentor_name, mentor_surname)

    @staticmethod
    def get_team_by_name(team_name):
        # TODO implement this
        pass

