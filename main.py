from flask import Flask, render_template, request, redirect, url_for, session, escape
from model.student import Student
from model.mentor import Mentor
from model.user import User
import sys

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
