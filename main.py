from flask import Flask, render_template, request, redirect, url_for
from model.student import Student
from model.mentor import Mentor
from model.team import Team
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


@app.route('/team_create.html', methods=['POST', 'GET'])
def create_team():
    # if request.method == 'GET':
    if request.method == 'POST':
        car_name = request.form['cars']
        print(car_name)
        team_name = request.form['new_team_name']
        member1 = request.form['member1']
        print(request.form.getlist('member1'))
        member2 = request.form['member2']
        member3 = request.form['member3']
        member4 = request.form['member4']

        member = [member1, member2, member3, member4]
        print(member)
        if len(team_name) > 0:
            Team.add_new_team(team_name, member)
        return redirect(url_for('display_teams'))
    return render_template('team_create.html', student_list=Student.get_list_of_students())


@app.route('/teams.html')
def display_teams():
    return render_template('teams.html', teams=Team.get_list_of_teams())


@app.route('/team_details/<int:team_id>')
def team_details(team_id):
    return render_template('team_details.html', person=Team.get_team_details(team_id))








if __name__ == "__main__":
    check_run_args()
    app.run(debug=True, port=1111)