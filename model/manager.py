from model.user import User
from main import db

class Manager(User, db.Model):

    # table name in database for SQLAlchemy
    __tablename__ = 'Manager'

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
