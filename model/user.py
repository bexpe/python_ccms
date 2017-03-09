from model.database import Database


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

    @classmethod
    def login(cls, login, passw):
        db = Database()

        query = ("""
        SELECT * from (SELECT id, name, Login, Password, 'student' as user_type FROM Student
                        UNION
                        SELECT id, Name, Login, Password, 'mentor' as user_type FROM Mentor
                        UNION
                        SELECT id, Name, Login, Password, 'employee' as user_type FROM Employee
                        UNION
                        SELECT id, Name, Login, Password, 'manager' as user_type FROM Manager)
                        where  Login = ? and  Password = ?
                    """)
        # awesome query, I love union <3

        values = ((login, passw))

        user = db.get(query, values)
        if not user:
            return
        user = db.get(query, values)[0]
        db.close()
        user_dict = {'id': user[0], 'name': user[1], 'type': user[4]}
        return user_dict
