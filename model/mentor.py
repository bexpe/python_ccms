from model.user import User
from model.database import Database


class Mentor(User):
    def __init__(self,user_id, name, surname, email, date_of_birth, city, phone, login):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)

    def get_mentor_by_id(self, id):
        pass

    def get_mentor_details(self, id):
        pass

    @classmethod
    def get_list_of_mentors(self):
        list_of_mentors = []
        db = Database()
        query = """SELECT * FROM Mentor;"""
        for person in db.get(query):
            person_object = Mentor(person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7])
            list_of_mentors.append(person_object)
        db.close()
        return list_of_mentors

    def edit_mentor(self, id):
        pass

    def add_new_mentor(self):
        pass
