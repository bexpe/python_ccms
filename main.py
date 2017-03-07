from flask import Flask, render_template, request, redirect
from model.student import Student
from model.mentor import Mentor

app = Flask(__name__)


@app.route("/")
def index():
    """ Shows list of todo items stored in the database.
    """
    return render_template('index.html')

@app.route('/teams')
def gdyuasguydg(error):
    """Closes the database again at the end of the request."""
    #Todo.close_database()
    pass

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
    students = Student.get_list_of_students()
    return render_template('student_list.html', students=students)

@app.route('/mentor_list.html')
def mentor_list():
    mentors = Mentor.get_list_of_mentors()
    return render_template('mentor_list.html', students=mentors)


if __name__ == "__main__":
    app.run(debug=True)
