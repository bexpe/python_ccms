from flask import Flask, render_template, request, redirect, session, url_for, escape
from model.assigment import Assigment
from model.assigment import Answer
from model.student import Student
from model.mentor import Mentor
from model.user import User
import sys
from datetime import datetime


app = Flask(__name__)


def check_run_args():
    try:
        if sys.argv[1] == '-d':
            from dump_db import dump_db
            dump_db()  # clearing db and inserting testing rows
    except IndexError:
        pass


@app.route('/')
def index():
    if 'user' in session:
        user = session['user']
        return render_template('index.html', user=user)
    return redirect(url_for('login'))


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
    assigments_list = Assigment.get_list_of_assigments()
    user = session['user']
    if user['type'] == 'Student':
        student = Student.get_student_by_id(user['id'])
        return render_template('assignment_list.html', assigments_list=assigments_list, user=user, student=student)
    return render_template('assignment_list.html', assigments_list=assigments_list, user=user)


@app.route("/submit_assigment/<assigment_id>", methods=['GET', 'POST'])
def submit_assigment(assigment_id):
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
    assigment = Assigment.get_assigment_by_id(assigment_id)
    if assigment.task_type == 'Personal':
        students_list = Student.get_list_of_students()
        return render_template('assignment_grade.html', assigment=assigment, students_list=students_list, user=user)
    elif assigment.task_type == 'Team':
        #team_list = Team.get_list_of_teams()
        return render_template('assignment_grade.html', assigment=assigment, user=user)


@app.route("/grade_answer/<answer_id>", methods=['POST'])
def grade_answer(answer_id):
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


if __name__ == "__main__":
    check_run_args()
    app.run(debug=True, port=1111)
