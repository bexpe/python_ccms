from model.database import *

class Team:

    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name

    @classmethod
    def add_new_team(cls, name):
        db = Database()
        new_team = Team(0, name)
        query = """INSERT INTO Teams(Name) VALUES (?)""", (new_team.name,)
        db.set(query)
        db.close()
        return new_team

    def edit_team(self, team_id, edit_new_name):
        db = Database()
        query = """UPDATE Teams SET Name = (?) WHERE ID=(?)""", (edit_new_name, team_id)
        db.set(query)
        db.close()

    def remove_team(self, team_id):
        db = Database()
        query = """DELETE FROM Teams WHERE ID=(?)""", (team_id,)
        db.set(query)
        db.close()

    def get_team_details(self, team_id):
        team_details = []
        db = Database()
        query = """SELECT * FROM Teams WHERE ID=(?)""", (team_id,)
        for team in db.get(query):
            team_object = Team(team[0], team[1])
            team_details.append(team_object)
        db.close()
        return team_details

    @classmethod
    def get_list_of_teams(cls):
        list_of_teams = []
        db = Database()
        query = """SELECT * FROM Teams"""
        for team in db.get(query):
            team_object = Team(team[0], team[1])
            list_of_teams.append(team_object)
        db.close()
        return list_of_teams

    def add_student_to_team(self, student_id, team_id):
        db = Database
        student_list_in_team = []
        query1 = """SELECT Name, Surname FROM Students WHERE ID= (?)""", (student_id,)
        student = db.get(query1)

        student_list_in_team.append(student)
        query2 = """ UPDATE Teams SET Members= student_list_in_team WHERE ID= (?)""", (team_id,)
        db.set(query2)
        db.close()
        return student_list_in_team

# edit = Team(0, 'Stefany')
# edit.edit_team(1, 'xd')
# edit.add_new_team('chvhv')
# print(edit.get_list_of_teams())
