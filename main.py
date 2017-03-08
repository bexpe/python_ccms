from flask import Flask, render_template, request, redirect
from model.student import Student
from model.mentor import Mentor
from model.team import Team

app = Flask(__name__)


@app.route("/")
def index():
    """ Shows list of todo items stored in the database.
    """
    return render_template('index.html')

@app.route('/teams')
def (error):
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

@app.route('/teams.html')
def teams():
    return render_template('teams.html', teams=Team.get_list_of_teams())

if __name__ == "__main__":
    app.run()
