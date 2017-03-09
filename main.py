from flask import Flask, render_template, request, redirect, url_for, session, escape
from model.student import Student
from model.mentor import Mentor
import sys

app = Flask(__name__)


def check_run_args():
    try:
        if sys.argv[1] == '-d':
            from dump_db import dump_db
            dump_db()  # clearing db and inserting testing rows
    except IndexError:
        pass


@app.before_request
def before_request():
    if 'user_id' in session and request.endpoint != 'login':
        if session['user_type'] == 'Student':
            user = Student.get_student_by_id(session['user_id'])
        elif session['user_type'] == 'Mentor':
            user = Mentor.get_mentor_by_id(session['user_id'])
        elif session['user_type'] == 'Manager':
            user = Manager.get_manager_by_id(session['user_id'])
        elif session['user_type'] == 'Employee':
            user = Employee.get_employee_by_id(session['user_id'])
    #return user


@app.route('/')
def index():
    if 'user' in session:
        user = session['user']
        return render_template('index.html', user=user)
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #User.login(request.form['email'], request.form['password'])
        user = Student.get_student_by_id(1)
        #mentor_logged = Mentor.get_mentor_by_id(1)
        #manager_logged = Manager.get_manager_by_id(1)
        #employee_logged = Employee.get_employee_by_id(1)
        user = {'id':user.user_id, 'name':user.name, 'type': user.__class__.__name__}
        session['user'] = user
        return redirect(url_for('index'))
    return render_template("login.html")


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
