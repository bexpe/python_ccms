from flask import Flask, render_template, request, redirect
from model.student import Student
from model.mentor import Mentor
import sys
from dump_db import dump_db
app = Flask(__name__)

def check_run_args():
    try:
        if sys.argv[1] == '-d':
            dump_db() # clearing db and inserting testing rows
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
    #Todo.close_database()
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


if __name__ == "__main__":
    check_run_args()
    app.run(debug=True, port=1111)
