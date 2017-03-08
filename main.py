from flask import Flask, render_template, request, url_for, redirect
from model.attendance import *
from model.student import *
app = Flask(__name__)

@app.route('/list')
def list():
    return render_template("xd.html", rows=Attendance.check_everyone_attendance())

@app.route('/attendance')
def attendance():
    print(Attendance.get_student_attendance(3))
    return render_template("attendance.html", rows=Attendance.get_student_attendance(3))

@app.route('/student_list.html')
def student_list():
    return render_template('student_list.html', students=Student.get_list_of_students())


@app.route('/check_attendance', methods=["POST", 'GET'])
def check_attendance():
    return render_template('check_attendance.html', students=Student.get_list_of_students())

@app.route('/present/<student_id>')
def obecny(student_id):
    Attendance.set_attendance(student_id, "Obecny")
    return redirect(url_for('check_attendance'))

@app.route('/absent/<student_id>')
def absent(student_id):
    Attendance.set_attendance(student_id, "Nieobecny")
    return redirect(url_for('check_attendance'))

@app.route('/late/<student_id>')
def late(student_id):
    Attendance.set_attendance(student_id, "Spozniony")
    return redirect(url_for('check_attendance'))

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
    app.run(debug=True)
