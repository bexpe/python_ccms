from model.database import Database
from main import db


class User():
    def __init__(self, user_id, name, surname, email, date_of_birth, city, phone, login):
        self.user_id = user_id
        self.email = email
        self.surname = surname
        self.name = name
        self.date_of_birth = date_of_birth
        self.city = city
        self.phone = phone
        self.login = login
        self.password = 'dupa'

    def __repr__(self):
        """Method for printing object in console in nice form
        :return: string: string with name and surname from person object
        """
        return "{} {}".format(self.name, self.surname)

    ######################  OLD LOGIN METHOD USING SQLITE (it is too beautiful for just delete it)
    # @classmethod
    # def login(cls, login, passw):
    #     db = Database()
    #     query = ("""
    #     SELECT * from (SELECT User_id, name, Login, Password, 'Student' as user_type FROM Student
    #                     UNION
    #                     SELECT User_id, Name, Login, Password, 'Mentor' as user_type FROM Mentor
    #                     UNION
    #                     SELECT User_id, Name, Login, Password, 'Employee' as user_type FROM Employee
    #                     UNION
    #                     SELECT User_id, Name, Login, Password, 'Manager' as user_type FROM Manager)
    #                     where  Login = ? and  Password = ?
    #                 """)
    #     values = ((login, passw))
    #
    #     user = db.get(query, values)
    #     if not user:
    #         return
    #     user = db.get(query, values)[0]
    #     db.close()
    #     user_dict = {'id': user[0], 'name': user[1], 'type': user[4]}
    #     return user_dict
    ######################

    def delete(self):
        """
        Delete object from database
        :return: none
        """
        db.session.delete(self)
        db.session.commit()

    def save(self):
        """
        Save new object in database
        :return: none
        """
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
        Update fileds of object in database
        :return: none
        """
        db.session.commit()
