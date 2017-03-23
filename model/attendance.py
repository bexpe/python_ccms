from model.database import *
from main import db
from datetime import date
import time

class Attendance(db.Model):
    __tablename__ = 'Attendance'
    attendance_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer)
    data = db.Column(db.String)
    attendance_value = db.Column(db.String)

    def __init__(self, attendence_id, student_id, data, attendence_value):
        self.student_id = student_id
        self.attendance_value = attendence_value
        self.attendance_id = attendence_id
        self.data = data

    @classmethod
    def get_student_attendance(cls, student_id):
        return cls.query.filter_by(student_id=student_id)

    @classmethod
    def set_attendance(cls, attendence_id, student_id, data, attendance_value):
        xd = date.today()
        if cls.query.filter_by(data=data('now')).filter_by(student_id=student_id):
            db.query(Attendance).update({Attendance.attendance_value: attendance_value})

        else:
            attendance = Attendance(attendence_id, student_id, xd, attendance_value)
            db.session.add(attendance)
        db.session.commit()

    @staticmethod
    def check_attendance_by_date(data_start, data_end, student_id):
        db = Database()
        check = db.get("SELECT Date, Attendance_value FROM Attendance WHERE Date BETWEEN (?) AND (?) AND Student_ID = (?)", (data_start, data_end, student_id))
        db.close()
        return check

    @staticmethod
    def check_everyone_attendance():
        db = Database()
        everyone = db.get("SELECT Attendance.Date, Student.Name, Student.Surname, Attendance.Attendance_value FROM Attendance INNER JOIN Student on Attendance.Student_ID = Student.ID")
        db.close()
        return everyone


