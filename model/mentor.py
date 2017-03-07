from model.user import User


class Mentor(User):
    def __init__(self,user_id, name, surname, email, date_of_birth, city, phone, login):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)

    def get_mentor_by_id(self, id):
        pass

    def get_mentor_details(self, id):
        pass

    def get_list_of_mentors(self):
        pass

    def edit_mentor(self, id):
        pass

    def add_new_mentor(self):
        pass