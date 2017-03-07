from flask import Flask, render_template, request, redirect


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


if __name__ == "__main__":
    app.run()
