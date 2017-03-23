from model.database import *
from model.student import Student
from main import db


class Team(db.Model):
    __tablename__ = 'Teams'  # table name in database for SQLAlchemy
    team_id = db.Column(db.Integer, primary_key=True)  # columns in table for SQLAlchemy
    team_name = db.Column(db.String)

    def __init__(self, team_name):
        self.team_name = team_name

    def save_new_team(self):
        """
        This method adding new team to the db and saving changes
        """
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
        This method is saving changes in an edited object to the database
        """
        db.session.commit()

    @classmethod
    def remove_team(cls, team_id):
        """
        This method removes a team from a database
        :param team_id:
        """
        team = Team.get_team_by_id(team_id)  # getting id of a team to remove
        db.session.delete(team)
        team_members = Team.get_list_of_students_by_team_id(team_id)  # getting team members from students by team id
        for student in team_members:
            student.set_team_id(student.user_id, 'None')  # changing a team id in students table
        db.session.commit()

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
        """
        Gets object of a team from the database
        :param team_id:
        :return: object of a team
        """
        return cls.query.get(team_id)

    @classmethod
    def get_list_of_teams(cls):
        """
        Gets a list of every team in a Team table from database
        :return: all teams objects
        """
        return Team.query.all()

    @classmethod
    def get_list_of_students_by_team_id(cls, team_id):
        """
        This method returns a list of students which have a specified id
        :param team_id:
        :return: a list of students which have specified id
        """
        team_members = []
        for student in Student.get_list_of_students():
            if student.team_id == team_id:  # looking for team members by id
                team_members.append(student)
        return team_members

    def get_team_students(self):
        """
        This method gets all students which belongs to the team specified and filtered by id
        :return:
        """
        return Student.query.filter_by(team_id=self.team_id)  # filtering all students and looking for theese which have
        # specified team id
