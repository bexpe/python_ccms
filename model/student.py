from model.user import User

class Student(User):
    def __init__(self, user_id, name, surname, email, date_of_birth, city, phone, login, team_id, card):
        super().__init__(user_id, name, surname, email, date_of_birth, city, phone, login)
        self.team_id = team_id
        self.card = card

