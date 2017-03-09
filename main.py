from flask import Flask, render_template, request, url_for, redirect
from model.attendance import *
from model.student import *
app = Flask(__name__)

@app.route('/list')
def list():
    return render_template("xd.html", rows=Attendance.check_everyone_attendance())

@app.route('/attendance_data/<student_id>?<start_date>?<end_date>')
def attendance_data(student_id, start_date, end_date):
    attendance = Attendance.check_attendance_by_date(start_date, end_date, student_id)
    attendance_lvl = 0
    x = 0
    for i in attendance:
        if i[1] == "Obecny":
            x += 1
            attendance_lvl += 100
        elif i[1] == "Spozniony":
            x += 1
            attendance_lvl += 80
        elif i[1] == "Nieobecny":
            x += 1
            attendance_lvl += 0
        continue
    if x != 0:
        attendance_lvl = attendance_lvl / x
        attendance_lvl = int(attendance_lvl)
    return render_template("attendance.html", rows=attendance, attendence_lvl=attendance_lvl, student_id=student_id)


@app.route('/attendance/<student_id>')
def attendance(student_id):
    attendance = Attendance.get_student_attendance(student_id)
    attendance_lvl = 0
    x = 0
    for i in attendance:
        if i[1] == "Obecny":
            x += 1
            attendance_lvl += 100
        elif i[1] == "Spozniony":
            x += 1
            attendance_lvl += 80
        elif i[1] == "Nieobecny":
            x += 1
            attendance_lvl += 0
        continue
    if x != 0:
        attendance_lvl = attendance_lvl / x
        attendance_lvl = int(attendance_lvl)
    return render_template("attendance.html", rows=attendance, attendence_lvl=attendance_lvl, student_id=student_id)


@app.route('/student_list.html')
def student_list():
    return render_template('student_list.html', students=Student.get_list_of_students())


@app.route('/check_attendance', methods=["POST", 'GET'])
def check_attendance():
    return render_template('check_attendance.html', students=Student.get_list_of_students())


@app.route('/present/<student_id>')
def present(student_id):
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


@app.route('/attendance_by_data', methods=['GET', 'POST'])
def data():
    if request.method == "POST":
        start_date = request.form.get("start")
        end_date = request.form.get("end")
        student_id = request.form.get("student_id")
        return redirect(url_for('attendance_data', student_id=student_id, start_date=start_date, end_date=end_date))
    return render_template('attendance_by_data.html')


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
