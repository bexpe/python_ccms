from flask import Flask, render_template, request, redirect, session, url_for, escape
from model.assigment import Assigment
from model.assigment import Answer
app = Flask(__name__)


@app.route("/")
def index():
    """ Shows list of todo items stored in the database.
    """
    return render_template('index.html')


@app.route("/assigments")
def assigments():
    assigments_list = Assigment.get_list_of_assigments()
    return render_template('assignment_list.html', assigments=assigments_list, student_id=1)


@app.route("/submit_assigment/<assigment_id>", methods=['GET', 'POST'])
def submit_assigment(assigment_id):
    if request.method == 'GET':
        return render_template('submit_assigment.html', assigment_id=assigment_id)
    else:
        student_answer = request.form['github_link']
        # TODO
        # 1 is student ID, to get from session
        Answer.submit_answer(student_answer, 1, assigment_id)
        return redirect('/assigments')


@app.route("/grade_assigment/<assigment_id>", methods=['GET', 'POST'])
def grade_assigment(assigment_id):
    if request.method == 'GET':
        return render_template('assignment_grade.html', assigment=Assigment.get_assigment_by_id(assigment_id))
    else:
        return redirect('/grade_assigment/{}'.format(assigment_id))


@app.route("/add_assigment", methods=['GET', 'POST'])
def add_new_assigment():
    if request.method == 'GET':
        return render_template('add_assigment.html')
    else:
        task_name = request.form['task-name']
        task_type = request.form['task-type']
        Assigment.add_new_assigment(task_name, task_type)
        return redirect('/assigments')


def redirect_url():
    """Return link to previous page"""
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')


if __name__ == "__main__":
    app.run()
