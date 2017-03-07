from model.user import User


class Mentor(User):
    def __init__(self,user_id, name, surname, email, date_of_birth, city, phone, login):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)
