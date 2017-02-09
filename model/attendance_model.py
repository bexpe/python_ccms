import sqlite3


class AttendanceModel:

    # TEMP BY SEBASTIAN
    @staticmethod
    def add_assignment_to_db(assignment_object):
        connect = sqlite3.connect('data/data.db')
        cur = connect.cursor()
        cur.execute("INSERT INTO Student_Attendance(Student_id, Date, Attendance_value) VALUES(?,?,?)",
                    (assignment_object.student_id, assignment_object.date, assignment_object.attendance))
        connect.commit()
        cur.execute("SELECT * FROM Student_Attendance")
        data = cur.fetchall()
        for row in data:
            print(row)

    @staticmethod
    def check_attendance_by_id_model(student_id):
        connect = sqlite3.connect('data/data.db')
        cur = connect.cursor()
        cur.execute("SELECT Attendance_value, Date FROM Student_Attendance WHERE Student_id = (?)", student_id)
        connect.commit()

    @staticmethod
    def count_attendance_values_model(student_id):