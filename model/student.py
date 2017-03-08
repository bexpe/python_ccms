
from model.user import User
from model.database import Database

class Student(User):
    def __init__(self, user_id, name, surname, email, date_of_birth, city, phone, login, team_id, card):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)
        self.team_id = team_id
        self.card = card

    def __repr__(self):
        return "{} {}".format(self.name, self.surname)

    @classmethod
    def get_list_of_students(cls):
        list_of_students = []
        db = Database()
        query = """SELECT * FROM Student;"""
        for person in db.get(query):
            person_object = Student(person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7], person[9], person[10])
            list_of_students.append(person_object)

        db.close()
        return list_of_students