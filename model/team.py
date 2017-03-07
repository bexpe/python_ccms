from model.database import *


class Team:

    def __init__(self):
        self.db = Database()

    def add_new_team(self, name):
        self.db.set("INSERT INTO Teams VALUES (NULL, (?))", (name,))

    def edit_team(self, team_id, edit_new_name):
        z = self.db.set("UPDATE Teams SET Name = (?) WHERE ID=(?)", (edit_new_name, team_id))

    def remove_team(self, team_id):
        self.db.set("DELETE FROM Teams WHERE ID=(?)", (team_id,))

    def get_team_details(self, team_id):
        self.db.get("SELECT * FROM Teams WHERE ID=(?)", (team_id,))

    def get_list_of_teams(self):
        self.db.get("SELECT * FROM Teams")

    def add_student_to_team(self, student_id, team_id):
        self.db.get(" Teams ")


edit = Team()
edit.edit_team(1, 'xd')
edit.add_new_team('chvhv')