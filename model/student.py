from model.user import User
from main import db


class Student(User, db.Model):

    # table name in database for SQLAlchemy
    __tablename__ = 'Student'

    # columns in table for SQLAlchemy
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    city = db.Column(db.String)
    phone = db.Column(db.String)
    login = db.Column(db.String)
    password = db.Column(db.String)
    team_id = db.Column(db.String)
    card = db.Column(db.String)

    def __init__(self, user_id, name, surname, email, date_of_birth, city, phone, login, team_id, card):
        User.__init__(self, user_id, name, surname, email, date_of_birth, city, phone, login)
        self.team_id = team_id
        self.card = card

    @classmethod
    def get_list_of_students(cls):
        """
        Retrieve person from table and return them in list of objects
        :return: list: list with person objects
        """
        return cls.query.all()

    def get_student_details(self):
        """
        This method gets details of specified student
        :return: a dictionary with information about student
        """
        return self.__dict__

    @classmethod
    def get_student_by_id(cls, idx):
        """
        Finds row in database by id and return object made with proper data
        :param idx: id of row in db
        :return: object: person object
        """
        return cls.query.get(idx)

    def set_team_id(self, student_id, team_id):
        """
        Looking for student with specified id and setting a new value of a team_id
        :param student_id:
        :param team_id:
        """
        student = Student.get_student_by_id(student_id)
        student.team_id = team_id
        student.save()
