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
            person_object = Student(person[0], person[1], person[2], person[3], person[4], person[5], person[6],
                                    person[7], person[9], person[10])
            list_of_students.append(person_object)

        db.close()
        return list_of_students

    def get_student_details(self):
        return self.__dict__

    def edit_student(self, student_object):
        db = Database()
        query = """UPDATE Student SET Name=(?), Surname=(?), Email=(?), Date_of_birth=(?), City=(?), Phone=(?), Login=(?), Team_ID=(?)  WHERE id =(?);"""
        db.get(query, (
            student_object.name,
            student_object.surname,
            student_object.email,
            student_object.date_of_birth,
            student_object.city,
            student_object.phone,
            student_object.login,
            student_object.team_id,
            student_object.user_id
        )
               )

    def add_new_student(self, student_object):
        db = Database()
        query = """INSERT INTO Mentor(Name, Surname, Email, Date_of_birth, City, Phone, Login) VALUES (?,?,?,?,?,?,?);"""
        db.get(query, (
            student_object.name,
            student_object.surname,
            student_object.email,
            student_object.date_of_birth,
            student_object.city,
            student_object.phone,
            student_object.login,
            student_object.user_id
        )
               )

    def save(self):
        db = Database()
        values = (
        self.name, self.surname, self.email, self.date_of_birth, self.city, self.phone, self.login, self.team_id,
        self.card, self.user_id)

        if not self.user_id:
            values = values[:-1]
            query = """INSERT INTO Student(Name, Surname, Email, Date_of_birth, City, Phone, Login, Team_ID, Card) VALUES (?,?,?,?,?,?,?,?,?);"""
        else:
            query = """UPDATE Student SET Name=(?), Surname=(?), Email=(?), Date_of_birth=(?), City=(?), Phone=(?), Login=(?), Team_ID=(?), Card=(?)  WHERE id =(?);"""

        db.set(query, values)
        db.close()

    @classmethod
    def get_student_by_id(cls, idx):
        db = Database()
        query = """SELECT * FROM Student WHERE id =(?)"""
        person = db.get(query, (idx,))[0]
        print(person)
        person_object = Student(person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7],
                                person[9], person[10])
        db.close()
        return person_object
