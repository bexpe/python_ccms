from model.database import *


class Team:

    def __init__(self, team_id, team_name):
        self.db = Database()
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

        z = self.db.set("UPDATE Teams SET Name = (?) WHERE ID=(?)", (edit_new_name, team_id))

    def remove_team(self, team_id):
        self.db.set("DELETE FROM Teams WHERE ID=(?)", (team_id,))

    def get_team_details(self, team_id):
        self.db.get("SELECT * FROM Teams WHERE ID=(?)", (team_id,))

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
        self.db.get(" Teams ")


edit = Team()
edit.edit_team(1, 'xd')
edit.add_new_team('chvhv')
print(edit.get_list_of_teams())
