from model.Mentor_model import Mentor_model


class Mentor(Employee):

    def __init__(self, name, surname, email, date_of_birth, city, phone):
        super().__init__(name, surname, email, date_of_birth, city, phone)

    def get_mentor_details(self):
        return self.get_details_basic()

    def remove_mentor(self):
        Mentor_model.remove_mentor(self.get_full_name())

    @staticmethod
    def get_mentors_list():
        list_of_mentors = Mentor_model.get_mentors_list()

    @staticmethod
    def add_new_mentor(name, surname, email, date_of_birth, city, phone):
        Mentor.add_new_mentor(name, surname, email, date_of_birth, city, phone)