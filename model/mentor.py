from model.user import User
from model.database import Database


class Mentor(User):
    def __init__(self,user_id, name, surname, email, date_of_birth, city, phone, login):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)

    def get_mentor_by_id(self, idx):
        db = Database()
        query = """SELECT * FROM Mentor WHERE id =(?)"""
        person = db.get(query, (idx,))
        new_mentor = Mentor(person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7])
        return new_mentor

    def get_mentor_details(self, idx):
        pass

    def get_list_of_mentors(cls):
        list_of_mentors = []
        db = Database()
        query = """SELECT * FROM Mentor;"""
        for person in db.get(query):
            person_object = Mentor(person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7])
            list_of_mentors.append(person_object)

        db.close()
        return list_of_mentors

    def edit_mentor(self, mentor_object):
        db = Database()
        query = """UPDATE Mentor SET Name=(?), Surname=(?), Email=(?), Date_of_birth=(?), City=(?), Phone=(?), Login=(?) WHERE id =(?);"""
        db.get(query, (
                        mentor_object.name,
                        mentor_object.surname,
                        mentor_object.email,
                        mentor_object.date_of_birth,
                        mentor_object.city,
                        mentor_object.phone,
                        mentor_object.login,
                        mentor_object.user_id
                        )
                )

    def add_new_mentor(self, mentor_object):
        db = Database()
        query = """INSERT INTO Mentor(Name, Surname, Email, Date_of_birth, City, Phone, Login) VALUES (?,?,?,?,?,?,?);"""
        person = db.get(query, (
                                mentor_object.name,
                                mentor_object.surname,
                                mentor_object.email,
                                mentor_object.date_of_birth,
                                mentor_object.city,
                                mentor_object.phone,
                                mentor_object.login,
                                mentor_object.user_id
                                )
                        )