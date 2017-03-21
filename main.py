from flask import Flask, render_template, request, redirect, session, url_for, escape
import sys
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


from model.assigment import Assigment
from model.assigment import Answer
from model.attendance import *
from model.student import Student
from model.mentor import Mentor
from model.team import Team
from model.user import User

################################################
# Attendance funcionality
################################################

@app.route('/attendance_data/<student_id>?<start_date>?<end_date>')
def attendance_data(student_id, start_date, end_date):
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    attendance = Attendance.check_attendance_by_date(start_date, end_date, student_id)
    attendance_lvl = 0
    x = 0
    for i in attendance:
        if i[1] == "Obecny":
            x += 1
            attendance_lvl += 100
        elif i[1] == "Spozniony":
            x += 1
            attendance_lvl += 80
        elif i[1] == "Nieobecny":
            x += 1
            attendance_lvl += 0
        continue
    if x != 0:
        attendance_lvl = attendance_lvl / x
        attendance_lvl = int(attendance_lvl)
    return render_template("attendance.html", user=user, rows=attendance, attendence_lvl=attendance_lvl,
                           student_id=student_id)


@app.route('/attendance/<student_id>')
def attendance(student_id):
    user = session['user']
    if user['type'] != 'Mentor' and user['id'] != student_id:
        student_id = user['id']
    attendance = Attendance.get_student_attendance(student_id)
    attendance_lvl = 0
    x = 0
    for i in attendance:
        if i[1] == "Obecny":
            x += 1
            attendance_lvl += 100
        elif i[1] == "Spozniony":
            x += 1
            attendance_lvl += 80
        elif i[1] == "Nieobecny":
            x += 1
            attendance_lvl += 0
        continue
    if x != 0:
        attendance_lvl = attendance_lvl / x
        attendance_lvl = int(attendance_lvl)
    return render_template("attendance.html", user=user, rows=attendance, attendence_lvl=attendance_lvl,
                           student_id=student_id)


@app.route('/student_list.html')
def student_list():
    user = session['user']
    if user['type'] in ('Mentor', 'Employee'):
        return render_template('student_list.html', user=user, students=Student.get_list_of_students())


@app.route('/check_attendance', methods=["POST", 'GET'])
def check_attendance():
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    return render_template('check_attendance.html', students=Student.get_list_of_students(), user=user)


@app.route('/present/<student_id>')
def present(student_id):
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    Attendance.set_attendance(student_id, "Obecny")
    return redirect(url_for('check_attendance'))


@app.route('/mentor_list.html')
def mentor_list():
    user = session['user']
    if user['type'] != 'Manager':
        return redirect(url_for('index'))
    return render_template('mentor_list.html', mentors=Mentor.get_list_of_mentors(), user=user)


@app.route('/edit_mentor/<int:user_id>', methods=['GET', 'POST'])
def edit_mentor(user_id):
    user = session['user']
    if user['type'] == 'Manager':
        mentor_url = "mentor_list"
        if request.method == "POST":
            login = request.form['login']
            email = request.form['email']
            name = request.form['name']
            surname = request.form['surname']
            date_of_birth = None
            city = None
            phone = None
            new_mentor = Mentor(user_id, name, surname, email, date_of_birth, city, phone, login)
            new_mentor.save()
            return redirect(url_for(mentor_url))
        return render_template('edit_mentor.html', person=Mentor.get_mentor_by_id(user_id), url=mentor_url, user=user)
    return redirect(url_for('error.html'))


@app.route('/edit_student/<int:user_id>', methods=['GET', 'POST'])
def edit_student(user_id):
    user = session['user']
    if user['type'] == 'Manager' or 'Mentor' or "Employee":
        student_url = "student_list"
        if request.method == "POST":
            login = request.form['login']
            email = request.form['email']
            name = request.form['name']
            surname = request.form['surname']
            date_of_birth = None
            city = None
            phone = None
            team_id = None
            card = None
            student = Student.get_student_by_id(user_id)
            student.login = login
            student.email = email
            student.name = name
            student.surname = surname

            student.update()
            db.session.commit()
            return redirect(url_for(student_url))
        return render_template('edit_student.html', person=Student.get_student_by_id(user_id), url=student_url, user=user)
    return redirect(url_for('error.html'))


@app.route('/add_mentor.html', methods=['GET', 'POST'])
def add_mentor():
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
            new_mentor = Mentor(user_id, name, surname, email, date_of_birth, city, phone, login)
            new_mentor.save()
            return redirect(url_for(mentor_url))
        return render_template('add_mentor.html', url=mentor_url, user=user)
    return redirect(url_for('error.html'))


@app.route('/add_student.html', methods=['GET', 'POST'])
def add_student():
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
            new_student = Student(user_id, name, surname, email, date_of_birth, city, phone, login, team_id, card)
            new_student.save()
            return redirect(url_for(student_url))
        return render_template('add_student.html', url=student_url, user=user)
    return redirect(url_for('error.html'))


@app.route('/details_mentor/<int:user_id>')
def details_mentor(user_id):
    user = session['user']
    if user['type'] == 'Manager':
        mentor_url = "mentor_list"
        return render_template('details_mentor.html', person=Mentor.get_mentor_by_id(user_id), url=mentor_url, user=user)
    return redirect(url_for('error.html'))


@app.route('/details_student/<int:user_id>')
def details_student(user_id):
    user = session['user']
    if user['type'] == 'Manager' or 'Manager' or "Employee":
        student_url = "student_list"
        return render_template('details_student.html', person=Student.get_student_by_id(user_id), url=student_url, user=user)
    return redirect(url_for('error.html'))


@app.route('/remove_mentor/<int:user_id>')
def remove_mentor(user_id):
    user = session['user']
    if user['type'] == 'Manager':
        mentor = Mentor.get_mentor_by_id(user_id)
        mentor.delete()
        return redirect(url_for('mentor_list'))
    return redirect(url_for('error.html'))


@app.route('/remove_student/<int:user_id>')
def remove_student(user_id):
    user = session['user']
    if user['type'] == 'Manager' or 'Mentor' or "Employee":
        student = Student.get_student_by_id(user_id)
        student.delete()
        return redirect(url_for('student_list'))
    return redirect(url_for('error.html'))


@app.route('/add_to_team/<int:user_id>')
def add_to_team(user_id):
    user = session['user']
    if user['type'] == 'Manager' or 'Mentor' or "Employee":
        pass  # TODO BEATA teams
    return redirect(url_for('error.html'))


@app.route('/error.html.html')
def privileges_error_handler():
    return render_template('error.html')


@app.route('/absent/<student_id>')
def absent(student_id):
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    Attendance.set_attendance(student_id, "Nieobecny")
    return redirect(url_for('check_attendance'))


@app.route('/late/<student_id>')
def late(student_id):
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    Attendance.set_attendance(student_id, "Spozniony")
    return redirect(url_for('check_attendance'))


@app.route('/check_everyone_attendance')
def check_everyone_attendance():
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    return render_template('check_everyone_attendance.html', user=user, rows=Attendance.check_everyone_attendance())


@app.route('/attendance_by_data', methods=['GET', 'POST'])
def data():
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    if request.method == "POST":
        start_date = request.form.get("start")
        end_date = request.form.get("end")
        student_id = request.form.get("student_id")
        return redirect(
            url_for('attendance_data', user=user, student_id=student_id, start_date=start_date, end_date=end_date))
    return render_template('attendance_by_data.html', user=user)


################################################
# Attendance funcionality END
################################################



def check_run_args():
    try:
        if sys.argv[1] == '-d':
            from dump_db import dump_db
            dump_db()  # clearing db and inserting testing rows
    except IndexError:
        pass


@app.route('/')
def index():
    user = session['user']
    return render_template('index.html', user=user)


@app.before_request
def before_request():
    if 'user' not in session and request.endpoint != 'login':
        return redirect(url_for('login'))
        #return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.login(request.form['email'], request.form['password'])
        if user:
            session['user'] = user
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    return render_template("login.html")


################################################
# Assigments funcionality
################################################


@app.route("/assigments")
def assigments():
    user = session['user']
    if user['type'] not in ('Mentor', 'Student'):
        return redirect(url_for('index'))
    assigments_list = Assigment.get_list_of_assigments()
    if user['type'] == 'Student':
        student = Student.get_student_by_id(user['id'])
        return render_template('assignment_list.html', assigments_list=assigments_list, user=user, student=student)
    return render_template('assignment_list.html', assigments_list=assigments_list, user=user)


@app.route("/submit_assigment/<assigment_id>", methods=['GET', 'POST'])
def submit_assigment(assigment_id):
    user = session['user']
    if user['type'] != 'Student':
        return redirect(url_for('index'))
    user = session['user']
    if request.method == 'GET':
        return render_template('submit_assigment.html', assigment_id=assigment_id, user=user)
    else:
        student_answer = request.form['github_link']
        Answer.submit_answer(student_answer, user['id'], assigment_id)
        return redirect('/assigments')


@app.route("/grade_assigment/<assigment_id>")
def grade_assigment(assigment_id):
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    assigment = Assigment.get_assigment_by_id(assigment_id)
    if assigment.task_type == 'Personal':
        students_list = Student.get_list_of_students()
        return render_template('assignment_grade.html', assigment=assigment, students_list=students_list, user=user)
    elif assigment.task_type == 'Team':
        team_list = Team.get_list_of_teams()
        return render_template('assignment_grade.html', assigment=assigment, team_list=team_list, user=user)


@app.route("/grade_answer/<answer_id>", methods=['POST'])
def grade_answer(answer_id):
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    answer = Answer.get_answer_by_id(answer_id)
    date_now = datetime.now()
    grade_date = "{}-{}-{}".format(date_now.year, date_now.month, date_now.day)
    answer.grade = request.form['grade']
    answer.grade_date = grade_date
    answer.save()
    return redirect(url_for('grade_assigment', assigment_id=answer.assigment_id))


@app.route("/add_assigment", methods=['GET', 'POST'])
def add_new_assigment():
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('add_assigment.html', user=user)
    else:
        task_name = request.form['task-name']
        task_type = request.form['task-type']
        Assigment.add_new_assigment(task_name, task_type)
        return redirect('/assigments')


################################################
# Assigments funcionality END
################################################


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('index'))


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/team_create.html', methods=['POST', 'GET'])
def create_team():
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    if request.method == 'POST':
        team_name = request.form['new_team_name']
        chosen_members = []
        member1 = request.form['member1']
        member2 = request.form['member2']
        member3 = request.form['member3']
        member4 = request.form['member4']
        if member1:
            chosen_members.append(Student.get_student_by_id(member1))
        if member2:
            chosen_members.append(Student.get_student_by_id(member2))
        if member3:
            chosen_members.append(Student.get_student_by_id(member3))
        if member4:
            chosen_members.append(Student.get_student_by_id(member4))
        if len(team_name) > 0:
            Team.add_new_team(team_name, chosen_members)
        return redirect('teams.html')
    return render_template('team_create.html', student_list=Student.get_list_of_students(), user=user)


@app.route('/teams.html')
def display_teams():
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    return render_template('teams.html', teams=Team.get_list_of_teams(), user=user)


@app.route("/remove/<int:team_id>")
def remove(team_id):
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    Team.remove_team(team_id)
    return redirect('teams.html')


@app.route('/team_details/<int:team_id>')
def team_details(team_id):
    user = session['user']
    if user['type'] != 'Mentor':
        return redirect(url_for('index'))
    return render_template('team_details.html', person=Team.get_team_details(team_id), user=user)

if __name__ == "__main__":
    check_run_args()
    app.run(debug=True, port=1111)
