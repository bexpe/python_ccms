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
    def add_new_team(cls, name, list_of_students):
        new_team = Team(None, name, '')

        db.session.add(new_team)

        for student in list_of_students:
            student.set_team_id(student.user_id, new_team.team_id)
        db.session.commit()
        return new_team

    def edit_team(self, team_id, edit_new_name):
        db.session.commit()

    @classmethod
    def get_team_by_id(cls, team_id):
        return cls.query.get(team_id)

    @classmethod
    def remove_team(cls, team_id):
        Team.get_team_by_id(team_id)
        db.session.delete()
        team_members = Team.get_list_of_students_by_team_id(team_id)
        for student in team_members:
            student.set_team_id(student.user_id, 'None')
        db.session.commit()


    @classmethod
    def get_list_of_teams(cls, team_id):

        teams = cls.query.all()
        for team in teams:
            team.members = Team.get_list_of_students_by_team_id(team.team_id)
        return teams


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

    @app.route('/team_edit/<int:team_id>', methods=['POST', 'GET'])  # z maina
    def team_edit(team_id):
        team = Team.get_team_by_id(team_id)

        if request.method == 'POST':
            team_name = request.form['edited_name']
            choosen_members = []
            member1 = request.form['member1']
            member2 = request.form['member2']
            member3 = request.form['member3']
            member4 = request.form['member4']
            if member1:
                choosen_members.append(Student.get_student_by_id(member1))
            if member2:
                choosen_members.append(Student.get_student_by_id(member2))
            if member3:
                choosen_members.append(Student.get_student_by_id(member3))
            if member4:
                choosen_members.append(Student.get_student_by_id(member4))
            if len(team_name) > 0:
                team_members = Team.get_list_of_students_by_team_id(team_id)
                team.edit_team(team_id, team_name, choosen_members, team_members)
            return redirect('teams.html')
        return render_template('team_edit.html', team=team, student_list=Student.get_list_of_students())