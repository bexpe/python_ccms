from main import db
from model.employee import *
from model.manager import *
from model.student import *
from model.mentor import *


class Login:

    @classmethod
    def login(cls, login, password):
        user = db.session.query(Employee).filter_by(login=login,password=password).first()
        print(user)
        if user:
          return {'name':user.name, 'type':user.__tablename__, 'id':user.user_id}
        user = db.session.query(Student).filter_by(login=login,password=password).first()
        if user:
          return {'name':user.name, 'type':user.__tablename__, 'id':user[0].user_id}
        user = db.session.query(Manager).filter_by(login=login,password=password).first()
        if user:
          return {'name':user.name, 'type':user.__tablename__, 'id':user.user_id}
        user = db.session.query(Employee).filter_by(login=login,password=password).first()
        if user:
          return {'name':user.name, 'type':user.__tablename__, 'id':user.user_id}



print(Login.login('miriam@e','dupa'))