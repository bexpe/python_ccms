from model.user import User
from main import db


class Mentor(User, db.Model):

    # table name in database for SQLAlchemy
    __tablename__ = 'Mentor'

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

    def __init__(self, user_id, name, surname, email, date_of_birth, city, phone, login):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)

    @classmethod
    def get_mentor_by_id(cls, idx):
        """
        Finds row in database by id and return object made with proper data
        :param idx: id of row in db
        :return: object: person object
        """
        return cls.query.get(idx)

    def get_mentor_details(self, idx):
        """
        Returns dictionary made from object
        :param idx: id of row in db
        :return: dict: dictionary made from object
        """
        return self.__dict__

    @classmethod
    def get_list_of_mentors(cls):
        """
        Retrieve person from table and return them in list of objects
        :return: list: list with person objects
        """
        return cls.query.all()


