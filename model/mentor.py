from model.user import User
from model.database import Database


class Mentor(User):
    def __init__(self, user_id, name, surname, email, date_of_birth, city, phone, login):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)

    @classmethod
    def get_mentor_by_id(cls, idx):
        db = Database()
        query = """SELECT * FROM Mentor WHERE id =(?)"""
        person = db.get(query, (idx,))[0]
        print(person)
        new_mentor = Mentor(person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7])
        return new_mentor

    def get_mentor_details(self, idx):
        return self.__dict__

    @classmethod
    def get_list_of_mentors(cls):
        list_of_mentors = []
        db = Database()
        query = """SELECT * FROM Mentor;"""
        for person in db.get(query):
            person_object = Mentor(person[0], person[1], person[2], person[3], person[4], person[5], person[6],
                                   person[7])
            list_of_mentors.append(person_object)

        db.close()
        return list_of_mentors

    def save(self):
        db = Database()
        values = (
        self.name, self.surname, self.email, self.date_of_birth, self.city, self.phone, self.login, self.user_id)

        if not self.user_id:
            values = values[:-1]
            query = """INSERT INTO Mentor(Name, Surname, Email, Date_of_birth, City, Phone, Login) VALUES (?,?,?,?,?,?,?);"""
        else:
            query = """UPDATE Mentor SET Name=(?), Surname=(?), Email=(?), Date_of_birth=(?), City=(?), Phone=(?), Login=(?) WHERE id =(?);"""

        db.set(query, values)
        db.close()


