# from main import db <- used for testing this method, uncomment in case of fire or terrible disaster
from model.employee import *
from model.manager import *
from model.student import *
from model.mentor import *


class Login:

    @classmethod
    def login(cls, login, password):
        """
        Find proper user from database and return dictionary with necessary user's data for session
        :param login: user login from login form
        :param password: user password from login form
        :return: dictionary: dictionary with data for flask session
        """

        for role in [Mentor, Student, Manager, Employee]:
            user = db.session.query(role).filter_by(login=login, password=password).first()
            if user:
                return {'name': user.name, 'type': user.__tablename__, 'id': user.user_id}
