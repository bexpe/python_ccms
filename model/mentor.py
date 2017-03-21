from model.user import User
from model.database import Database
from main import db

class Mentor(User, db.Model):

    __tablename__ = 'Mentor'

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
        User.__init__(user_id, name, surname, email, date_of_birth, city, phone, login)

    @classmethod
    def get_mentor_by_id(cls, idx):
        return cls.query.get(idx)

    def get_mentor_details(self, idx):
        return self.__dict__

    @classmethod
    def get_list_of_mentors(cls):
        return cls.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()


