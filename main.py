from flask import Flask, render_template, request, redirect, url_for, session, escape
from model.student import Student
from model.mentor import Mentor
import sys

app = Flask(__name__)

def check_run_args():
    try:
        if sys.argv[1] == '-d':
            from dump_db import dump_db
            dump_db() # clearing db and inserting testing rows
    except IndexError:
        pass


@app.route('/')
def index():
    if 'username' in session:
        session['username']
        return render_template('index.html', user=user)
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/student_list.html')
def student_list():
    return render_template('student_list.html', students=Student.get_list_of_students())

@app.route('/mentor_list.html')
def mentor_list():
    return render_template('mentor_list.html', mentors=Mentor.get_list_of_mentors())

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_mentor(user_id):
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
        return render_template('edit.html', person=Mentor.get_mentor_by_id(user_id), url=mentor_url)
    else:
        return render_template('edit.html', person=Mentor.get_mentor_by_id(user_id), url=mentor_url)

def edit_student(user_id):
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
        new_student = Student(user_id, name, surname, email, date_of_birth, city, phone, login, team_id, card)
        new_student.save()
        return render_template('edit.html', person=Student.get_student_by_id(user_id), url=student_url)
    else:
        return render_template('edit.html', person=Student.get_student_by_id(user_id), url=student_url)

@app.route('/add.html', methods=['GET', 'POST'])
def add_mentor():
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
    else:
        return render_template('add.html', url=mentor_url)

def add_student():
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
    else:
        return render_template('add.html', url=student_url)

@app.route('/details/<int:user_id>')
def details_mentor(user_id):
    mentor_url = "mentor_list"
    return render_template('details.html', person=Mentor.get_mentor_by_id(user_id), url=mentor_url)

def details_student(user_id):
    student_url = "student_list"
    return render_template('details.html', person=Student.get_student_by_id(user_id), url=student_url)

@app.route('/remove/<int:user_id>')
def remove_mentor(user_id):
    mentor = Mentor.get_mentor_by_id(user_id)
    mentor.delete()
    return redirect(url_for('mentor_list'))

def remove_student(user_id):
    student = Student.get_student_by_id(user_id)
    student.delete()
    return redirect(url_for('student_list'))


if __name__ == "__main__":
    check_run_args()
    app.run(debug=True, port=1111)
