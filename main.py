from flask import Flask, render_template, request, redirect, session, url_for, escape
import sys
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from model.assignment import Assignment
from model.assignment import Answer
from model.attendance import *
from model.student import Student
from model.mentor import Mentor
from model.team import Team
from model.user import User
from utils.validation import Validate
from utils.login import Login


################################################
# Attendance
################################################


@app.route('/attendance_data/<student_id>?<start_date>?<end_date>')
def attendance_data(student_id, start_date, end_date):
    """
    This method gives possibility to check attendance of every student displayed
    :param student_id: int(id of searching student)
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    attendance = Attendance.check_attendance_by_date(start_date, end_date, student_id)
    attendance_lvl = 0
    x = 0
    for i in attendance:
        if i.attendance_value == "Obecny":
            x += 1
            attendance_lvl += 100
        elif i.attendance_value == "Spozniony":
            x += 1
            attendance_lvl += 80
        elif i.attendance_value == "Nieobecny":
            attendance_lvl += 0
        continue
    if x != 0:
        attendance_lvl = attendance_lvl / x
        attendance_lvl = int(attendance_lvl)
    return render_template("attendance.html", user=user, rows=attendance, attendence_lvl=attendance_lvl,
                           student_id=student_id)


@app.route('/attendance/<student_id>')
def attendance(student_id):
    """
    This method gives the possibility to show attendance level of a specified student
    :param student_id: int
    :return: render temple for html site with attendance detalis
    """
    user = session['user']
    if user['type'] != 'Mentor' and user['id'] != student_id:
        student_id = user['id']
    attendance = Attendance.get_student_attendance(student_id)
    attendance_lvl = 0
    x = 0
    for i in attendance:
        if i.attendance_value == "Obecny":
            x += 1
            attendance_lvl += 100
        elif i.attendance_value == "Spozniony":
            x += 1
            attendance_lvl += 80
        elif i.attendance_value == "Nieobecny":
            attendance_lvl += 0
        continue
    if x != 0:
        attendance_lvl = attendance_lvl / x
        attendance_lvl = int(attendance_lvl)
    return render_template("attendance.html", user=user, rows=attendance, attendence_lvl=attendance_lvl,
                           student_id=student_id)


@app.route('/check_attendance', methods=["POST", 'GET'])
def check_attendance():
    """
    Route for page with attendance checker
    :return: rendered webpage

    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    return render_template('check_attendance.html', students=Student.get_list_of_students(), user=user)


@app.route('/present/<student_id>')
def present(student_id):
    """
    set student status as present (obecny)
    :param student_id: int
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    attendance = Attendance(None, student_id, datetime.now().date(), "Obecny")
    attendance.save()
    return redirect(url_for('check_attendance'))


@app.route('/absent/<student_id>')
def absent(student_id):
    """
    set student status as absent (Nieobecny)
    :param student_id: int
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    attendance = Attendance(None, student_id, datetime.now().date(), "Nieobecny")
    attendance.save()
    return redirect(url_for('check_attendance'))


@app.route('/late/<student_id>')
def late(student_id):
    """
    set student status as late (Spozniony)
    :param student_id: int
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    attendance = Attendance(None, student_id, datetime.now().date(), "Spozniony")
    attendance.save()
    return redirect(url_for('check_attendance'))


@app.route('/check_everyone_attendance')
def check_everyone_attendance():
    """
    Return render template for check everyone attendece where we have list of all students
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    return render_template('check_everyone_attendance.html', user=user, rows=Attendance.check_everyone_attendance())


@app.route('/attendance_by_data', methods=['GET', 'POST'])
def data():
    """
    Check attendance by data
    :return: url for site with data
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    if request.method == "POST":
        start_date = request.form["start"]
        end_date = request.form["end"]
        student_id = request.form["student_id"]
        validated_object = Validate.date_validation(start_date, end_date, student_id)
        if validated_object.valid_object():
            return redirect(url_for('attendance_data',
                                    user=user,
                                    validated=validated_object))
        return render_template('attendance_by_data_validation.html',
                               user=user,
                               validated=validated_object)
    return render_template('attendance_by_data.html',
                           user=user)


################################################
# Students
################################################


@app.route('/student_list.html')
def student_list():
    """
    Route for page with list of person
    :return: rendered webpage
    """
    user = session['user']
    if user['type'] in ('Mentor', 'Employee'):
        return render_template('student_list.html', user=user, students=Student.get_list_of_students())


@app.route('/edit_student/<int:user_id>', methods=['GET', 'POST'])
def edit_student(user_id):
    """
    Edit person object atributes with validated data
    :param user_id: id of user
    :return:
    """
    user = session['user']
    if user['type'] == 'Manager' or 'Mentor' or "Employee":
        student_url = "student_list"
        if request.method == "POST":
            login = request.form['login']
            email = request.form['email']
            name = request.form['name']
            surname = request.form['surname']
            validated_object = Validate.edit_add_input(login, email, name, surname)
            if validated_object.valid_object():
                student = Student.get_student_by_id(user_id)
                student.login = validated_object.login
                student.email = validated_object.email
                student.name = validated_object.name
                student.surname = validated_object.surname

                student.update()
                return redirect(url_for(student_url))
            return render_template('edit_student.html',
                                   person=validated_object,
                                   url=student_url,
                                   user=user)
        return render_template('edit_student.html',
                               person=Student.get_student_by_id(user_id),
                               url=student_url,
                               user=user)
    return redirect(url_for('error.html'))



@app.route('/add_student.html', methods=['GET', 'POST'])
def add_student():
    """
    Create student object from data from form on webpage and store it in db
    :return:
    """
    user = session['user']
    if user['type'] == 'Manager' or 'Mentor' or "Employee":
        student_url = "student_list"
        if request.method == "POST":
            user_id = None
            login = request.form['login']
            email = request.form['email']
            name = request.form['name']
            surname = request.form['surname']
            date_of_birth = None
            city = None
            phone = None
            team_id = None
            card = None
            validated_object = Validate.edit_add_input(login, email, name, surname)
            if validated_object.valid_object():
                login = validated_object.login
                email = validated_object.email
                name = validated_object.name
                surname = validated_object.surname
                new_student = Student(user_id, name, surname, email, date_of_birth, city, phone, login, team_id,
                                      card)
                new_student.save()
                return redirect(url_for(student_url))
            return render_template('add_student_changed.html',
                                   person=validated_object,
                                   url=student_url,
                                   user=user)
        return render_template('add_student.html',
                               url=student_url,
                               user=user)
    return redirect(url_for('error.html'))


@app.route('/details_student/<int:user_id>')
def details_student(user_id):
    """
    Presents data of person
    :param user_id: id of student
    :return:
    """
    user = session['user']
    if user['type'] == 'Manager' or 'Manager' or "Employee":
        student_url = "student_list"
        return render_template('details_student.html', person=Student.get_student_by_id(user_id), url=student_url, user=user)
    return redirect(url_for('error.html'))


@app.route('/remove_student/<int:user_id>')
def remove_student(user_id):
    """
    Get user object and delete it from db
    :param user_id: id of user
    :return: template with a new list of students
    """
    user = session['user']
    if user['type'] == 'Manager' or 'Mentor' or "Employee":
        student = Student.get_student_by_id(user_id)
        student.delete()
        return redirect(url_for('student_list'))
    return redirect(url_for('error.html'))


################################################
# Mentors
################################################


@app.route('/mentor_list.html')
def mentor_list():
    """
    Route for page with list of person
    :return: rendered webpage
    """
    user = session['user']
    if user['type'] != 'Manager':
        return redirect(url_for('index'))
    return render_template('mentor_list.html', mentors=Mentor.get_list_of_mentors(), user=user)


@app.route('/edit_mentor/<int:user_id>', methods=['GET', 'POST'])
def edit_mentor(user_id):
    """
    Edit person object atributes with validated data
    :param user_id: id of user
    :return:
    """
    user = session['user']
    if user['type'] == 'Manager':
        mentor_url = "mentor_list"
        if request.method == "POST":
            login = request.form['login']
            email = request.form['email']
            name = request.form['name']
            surname = request.form['surname']
            validated_object = Validate.edit_add_input(login, email, name, surname)
            if validated_object.valid_object():
                mentor = Mentor.get_student_by_id(user_id)
                mentor.login = validated_object.login
                mentor.email = validated_object.email
                mentor.name = validated_object.name
                mentor.surname = validated_object.surname

                mentor.update()
                return redirect(url_for(mentor_url))
            return render_template('edit_student.html', person=validated_object,
                                   url=mentor_url, user=user)
        return render_template('edit_student.html', person=Mentor.get_student_by_id(user_id),
                               url=mentor_url, user=user)
    return redirect(url_for('error.html'))


@app.route('/add_mentor.html', methods=['GET', 'POST'])
def add_mentor():
    """
    Create student object from data from form on webpage and store it in db
    :return: different templates depending on information we want to display to the user
    """
    user = session['user']
    if user['type'] == 'Manager':
        mentor_url = "mentor_list"
        if request.method == "POST":
            user_id = None
            login = request.form['login']
            email = request.form['email']
            name = request.form['name']
            surname = request.form['surname']
            date_of_birth = None
            city = None
            phone = None
            validated_object = Validate.edit_add_input(login, email, name, surname)
            if validated_object.valid_object():
                login = validated_object.login
                email = validated_object.email
                name = validated_object.name
                surname = validated_object.surname
                new_mentor = Mentor(user_id, name, surname, email, date_of_birth, city, phone, login)
                new_mentor.save()
                return redirect(url_for(mentor_url))
            return render_template('add_mentor_changed.html',
                                   person=validated_object,
                                   url=mentor_url,
                                   user=user)
        return render_template('add_mentor.html',
                               url=mentor_url,
                               user=user)
    return redirect(url_for('error.html'))


@app.route('/details_mentor/<int:user_id>')
def details_mentor(user_id):
    """
    Presents data of person
    :param user_id: id of student
    :return:template with mentor details
    """
    user = session['user']
    if user['type'] == 'Manager':
        mentor_url = "mentor_list"
        return render_template('details_mentor.html', person=Mentor.get_mentor_by_id(user_id), url=mentor_url, user=user)
    return redirect(url_for('error.html'))


@app.route('/remove_mentor/<int:user_id>')
def remove_mentor(user_id):
    """
    Get user object and delete it from db
    :param user_id: id of user
    :return:
    """
    user = session['user']
    if user['type'] == 'Manager':
        mentor = Mentor.get_mentor_by_id(user_id)
        mentor.delete()
        return redirect(url_for('mentor_list'))
    return redirect(url_for('error.html'))


################################################
# Assigmnents
################################################


@app.route("/assignments")
def assignments():
    """
    Show list of assigments to grade or submit if you are student
    """
    user = session['user']
    if user['type'] not in ('Mentor', 'Student'):
        return redirect(url_for('index'))
    assignments_list = Assignment.get_list_of_assignments()
    if user['type'] == 'Student':
        student = Student.get_student_by_id(user['id'])
        return render_template('assignment_list.html', assignments_list=assignments_list, user=user, student=student)
    return render_template('assignment_list.html', assignments_list=assignments_list, user=user)


@app.route("/submit_assignment/<assignment_id>", methods=['GET', 'POST'])
def submit_assignment(assignment_id):
    """
    Student submit assignment handler.
    """
    user = session['user']
    if user['type'] != 'Student':
        return redirect(url_for('index'))
    user = session['user']
    if request.method == 'GET':
        return render_template('submit_assignment.html', assignment_id=assignment_id, user=user)
    else:
        assignment = Assignment.get_assignment_by_id(assignment_id)
        student = Student.get_student_by_id(user['id'])
        student_answer = request.form['github_link']
        if assignment.task_type == 'Personal':
            new_answer = Answer(student_answer, assignment_id, student_id=student.user_id)
        else:
            new_answer = Answer(student_answer, assignment_id, team_id=student.team_id)
        new_answer.save()
        return redirect('/assignments')


@app.route("/grade_assignment/<assignment_id>")
def grade_assignment(assignment_id):
    """
    Show list of answers to given assignment.
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    assignment = Assignment.get_assignment_by_id(assignment_id)
    if assignment.task_type == 'Personal':
        students_list = Student.get_list_of_students()
        return render_template('assignment_grade.html', assignment=assignment, students_list=students_list, user=user)
    elif assignment.task_type == 'Team':
        team_list = Team.get_list_of_teams()
        return render_template('assignment_grade.html', assignment=assignment, team_list=team_list, user=user)


@app.route("/grade_answer/<answer_id>", methods=['POST'])
def grade_answer(answer_id):
    """
    Grade answer by given id.
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    answer = Answer.get_answer_by_id(answer_id)
    date_now = datetime.now()
    grade_date = "{}-{}-{}".format(date_now.year, date_now.month, date_now.day)
    grade = request.form['grade']
    grade = Validate.grade_input(grade)
    if type(grade) != str:
        return redirect(url_for('grade_assignment', assignment_id=answer.assignment_id))
    answer.grade = grade
    answer.grade_date = grade_date
    answer.update()
    return redirect(url_for('grade_assignment', assignment_id=answer.assignment_id))


@app.route("/add_assignment", methods=['GET', 'POST'])
def add_new_assignment():
    """
    Adding new assignment to database.
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('add_assignment.html', user=user)
    else:
        task_name = request.form['task-name']
        task_name = Validate.add_assignment_input(task_name)
        if type(task_name) != str:
            return render_template('add_assignment.html', user=user)
        task_type = request.form['task-type']
        new_assignment = Assignment(task_name, task_type)
        new_assignment.save()
        return redirect('/assignments')

################################################
# Teams
################################################


@app.route('/team_create.html', methods=['POST', 'GET'])
def create_team():
    """
    Create team object from data from form on webpage and store it in db
    :return: list of teams with a new created team
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    if request.method == 'POST':
        team_name = request.form['new_team_name']
        team_name = Validate.team_input(team_name)
        if type(team_name) != str:
            return render_template('team_create.html',
                           student_list=Student.get_list_of_students(),
                           user=user)
        new_team = Team(team_name)
        new_team.save_new_team()
        members_id_list = [request.form['member1'],
                           request.form['member2'],
                           request.form['member3'],
                           request.form['member4']]
        for member_id in members_id_list:
            student = Student.get_student_by_id(member_id)
            if student:
                student.team_id = new_team.team_id
                student.update()
        return redirect('teams.html')
    return render_template('team_create.html',
                           student_list=Student.get_list_of_students(),
                           user=user)


@app.route('/team_edit/<int:team_id>', methods=['POST', 'GET'])  # z maina
def team_edit(team_id):
    """
    Edit team object atributes with validated data
    :param user_id: id of team
    :return:
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    team_to_edit = Team.get_team_by_id(team_id)
    if request.method == 'POST':
        if team_to_edit:
            team_name = request.form['edited_name']
            team_name = Validate.team_input(team_name)
            if type(team_name) != str:
                return render_template('team_edit.html',
                                       team=team_to_edit,
                                       student_list=Student.get_list_of_students(),
                                       user=user)
            # remove students from team \/
            old_students_in_team = team_to_edit.get_team_students()
            for old_student in old_students_in_team:
                old_student.team_id = None
                old_student.update()
            # update team name and insert new students to team
            # it means give each student team_id value
            team_to_edit.team_name = team_name
            team_to_edit.update()
            members_id_list = [request.form['member1'],
                               request.form['member2'],
                               request.form['member3'],
                               request.form['member4']]
            if any(members_id_list):  # if there is id in any member form
                for member_id in members_id_list:
                    student = Student.get_student_by_id(member_id)
                    if student:
                        student.team_id = team_to_edit.team_id
                        student.update()
        return redirect('teams.html')

    return render_template('team_edit.html',
                           team=team_to_edit,
                           student_list=Student.get_list_of_students(),
                           user=user, members=Team.get_list_of_students_by_team_id(team_id))


@app.route('/teams.html')
def display_teams():
    """
    Route for page with list of teams
    :return: rendered webpage
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    return render_template('teams.html', teams=Team.get_list_of_teams(), user=user)


@app.route("/remove/<int:team_id>")
def remove(team_id):
    """
    Get team object and delete it from db
    :param user_id: id of team
    :return:template with list of teams without newly removed team
    """
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    Team.remove_team(team_id)
    return redirect('teams.html')


################################################
# Login
################################################


def check_run_args():
    """
    This method is clearing a database from all data inserted by typeing in a console -d  by running the file
    """
    try:
        if sys.argv[1] == '-d':
            from dump_db import dump_db
            dump_db()  # clearing db and inserting testing rows
    except IndexError:
        pass


@app.route('/')
def index():
    """
    Shows main page after signing in
    :return: template with a main page after signing in
    """
    user = session['user']
    return render_template('index.html', user=user)


@app.before_request
def before_request():
    """
    Shows a page to sign in
    :return: template to sign in
    """
    if 'user' not in session and request.endpoint != 'login':
        return redirect(url_for('login'))
        # return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Gets data from login form and run method to compare it with data stored in db
    :return: if a user is finded its a template for this user if not- a template with a page to sign in again
    """
    from utils.internal_validation import ValidateInternal
    if request.method == 'POST':
        #TODO: fix db and change validation from ValidateInternal to Validate class.

        login = request.form['email']
        login = ValidateInternal.initial_check(login)
        password = request.form['password']
        password = ValidateInternal.initial_check(password)
        if type(login) != str or type(password) != str:
            return redirect(url_for('login'))
        user = Login.login(request.form['email'], request.form['password'])
        if user:
            session['user'] = user
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/logout')
def logout():
    """
    This method removes a username from the session if it is there and finishes a session
    :return: the template with an index page
    """
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('index'))


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/error.html.html')
def privileges_error_handler():
    """
    Shows an error template
    :return: error template
    """
    return render_template('error.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, port=1111)
