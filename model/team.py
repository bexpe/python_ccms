from model.database import *
from model.student import Student
from main import db

class Team(db.Model):
    # table name in database for SQLAlchemy
    __tablename__ = 'Teams'

    # columns in table for SQLAlchemy
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String)

    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name


    @classmethod
    def add_new_team(cls, name, list_of_students):  # SQL
        new_team = Team(None, name)

        db.session.add(new_team)

        for student in list_of_students:
            student.set_team_id(student.user_id, new_team.team_id)
        db.session.commit()
        return new_team


    # def edit_team(self, team_id, edit_new_name, choosen_members, list_of_students):
    #     print(self.__dict__)
    #     db = Database()
    #     self.team_id=team_id
    #     self.team_name=edit_new_name
    #     self.members=choosen_members
    #     print(self.__dict__)
    #     query = """UPDATE Teams SET Name = (?) WHERE ID=(?)"""
    #     values = (self.team_name, self.team_id)
    #     db.set(query, values)
    #     db.close()
    #     for student in list_of_students:
    #         student.set_team_id(student.user_id, self.team_id)

    def edit_team(self, team_id, edit_new_name):
        db.session.commit()

    @classmethod
    def remove_team(cls, team_id):  #                                    sql
        team = Team.get_team_by_id(team_id)
        db.session.delete(team)
        team_members = Team.get_list_of_students_by_team_id(team_id)
        for student in team_members:
            student.set_team_id(student.user_id, 'None')
        db.session.commit()

    # def get_team_details(self, team_id):
    #     team_details = []
    #     db = Database()
    #     query = """SELECT * FROM Teams WHERE ID=(?)""", (team_id,)
    #     for team in db.get(query):
    #         team_object = Team(team[0], team[1], team[2])
    #         team_details.append(team_object)
    #     db.close()
    #     return team_details

    # @classmethod
    # def get_team_by_id(cls, team_id):
    #     db = Database()
    #     query = """SELECT * FROM Teams WHERE ID=(?)"""
    #     values = (team_id,)
    #
    #     team = db.get(query, values)[0]
    #     print(team)
    #     team_object = Team(team[0], team[1], [])
    #     return team_object

    @classmethod
    def get_team_by_id(cls, team_id):
        return cls.query.get(team_id)


    @classmethod  # sql
    def get_list_of_teams(cls):
        print('qwertyui')

        # for team in teams:
        #     team.members = Team.get_list_of_students_by_team_id(team.team_id)
        return Team.query.all()


    @classmethod
    def get_list_of_students_by_team_id(cls, team_id):
        team_members = []
        for student in Student.get_list_of_students():
            if student.team_id == team_id:
                team_members.append(student)
        return team_members


# Team.add_student_to_team(1, 2)
print()

