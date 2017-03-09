from model.database import *
from model.student import Student

class Team:

    def __init__(self, team_id, team_name, members):
        self.team_id = team_id
        self.team_name = team_name
        self.members = members

    @classmethod
    def add_new_team(cls, name, list_of_students):
        db = Database()
        print(list_of_students)
        new_team = Team(None, name, '')
        query = """INSERT INTO Teams(Name)  VALUES (?)"""
        values = [new_team.team_name]
        new_team.team_id = db.set(query, values)
        db.close()
        for student in list_of_students:
            student.set_team_id(student.user_id, new_team.team_id)
        return new_team

    # def add_student_to_team(self, student_id, team_id):
    #         Student.get_student_by_id(student_id).team_id = team_id
    #         Student.save()

    def edit_team(self, team_id, edit_new_name):
        db = Database()
        query = """UPDATE Teams SET Name = (?) WHERE ID=(?)""", (edit_new_name, team_id)
        db.set(query)
        db.close()

    @classmethod
    def remove_team(cls, team_id):
        db = Database()
        team_members = Team.get_list_of_students_by_team_id(team_id)
        for student in team_members:
            student.set_team_id(student.user_id, 'NULL')

        query = """DELETE FROM Teams WHERE ID=(?)"""
        db.set(query, (team_id,))
        db.close()

    def get_team_details(self, team_id):
        team_details = []
        db = Database()
        query = """SELECT * FROM Teams WHERE ID=(?)""", (team_id,)
        for team in db.get(query):
            team_object = Team(team[0], team[1], team[2])
            team_details.append(team_object)
        db.close()
        return team_details

    @classmethod
    def get_list_of_teams(cls):
        list_of_teams = []
        db = Database()
        query = """SELECT * FROM Teams"""
        for team in db.get(query):
            team_id = team[0]
            team_name = team[1]
            team_members = Team.get_list_of_students_by_team_id(team_id)
            team_members_names = []
            for member in team_members:
                team_members_names.append(member.name + ' ' + member.surname)
            team_object = Team(team_id, team_name, team_members)

            list_of_teams.append(team_object)
        db.close()
        return list_of_teams

    # def add_student_to_team(cls, student_id, team_id):
    #     db = Database
    #     student_list_in_team = self.members
    #     query1 = """SELECT Name, Surname FROM Students WHERE ID= (?)""", (student_id,)
    #     student = db.get(query1)
    #
    #     student_list_in_team.append(student)
    #     query2 = """ UPDATE Teams SET Members= student_list_in_team WHERE ID= (?)""", (team_id,)
    #     db.set(query2)
    #     db.close()
    #     return student_list_in_team

    @classmethod
    def get_list_of_students_by_team_id(cls, team_id):
        team_members = []
        for student in Student.get_list_of_students():
            if student.team_id == team_id:
                team_members.append(student)
        return team_members

# Team.add_student_to_team(1, 2)
print()

