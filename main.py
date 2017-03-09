from flask import Flask, render_template, request, redirect, url_for
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


@app.route("/")
def index():
    """ Shows list of todo items stored in the database.
    """
    return render_template('index.html')


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    # Todo.close_database()
    pass


def redirect_url():
    """Return link to previous page"""
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')


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
        return redirect(url_for('mentor_list'))
    else:
        return render_template('add.html', url=mentor_url)

@app.route('/details/<int:user_id>')
def details_mentor(user_id):
    mentor_url = "mentor_list"
    return render_template('details.html', person=Mentor.get_mentor_by_id(user_id), url=mentor_url)

@app.route('/remove/<int:user_id>')
def remove_mentor(user_id):
    mentor = Mentor.get_mentor_by_id(user_id)
    mentor.delete()
    return redirect(url_for('mentor_list'))


@app.route('/edit_student/<int:user_id>')
def edit_student(user_id):
    return render_template('edit_student.html', person=Student.get_student_by_id(user_id))


@app.route('/details_student/<int:user_id>')
def details_student(user_id):
    return render_template('details_student.html', person=Student.get_student_by_id(user_id))


@app.route('/add_student.html')
def add_student():
    return render_template('add_student.html')


if __name__ == "__main__":
    check_run_args()
    app.run(debug=True, port=2222)
