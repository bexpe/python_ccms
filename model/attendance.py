from model.database import *
from main import db
from datetime import *
import time


class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer)
    date = db.Column(db.INTEGER)
    attendance_value = db.Column(db.String)

    def __init__(self, id, student_id, data, attendance_value):
        self.student_id = student_id
        self.attendance_value = attendance_value
        self.attendance_id = id
        self.data = data

    @classmethod
    def get_student_attendance(cls, student_id):
        return cls.query.filter_by(student_id=student_id)

    @classmethod
    def set_attendance(cls, attendence_id, student_id, date, attendance_value):
        if cls.query.filter_by(date=date).filter_by(student_id=student_id):
            
        else:
            attendance = Attendance(attendence_id, student_id, date, attendance_value)
            db.session.add(attendance)
        db.session.commit()

    @classmethod
    def check_attendance_by_date(cls, data_start, data_end, student_id):
        return cls.query.filter_by(student_id=student_id).filter_by(date > data_start)
        # ("SELECT Date, Attendance_value FROM Attendance WHERE Date BETWEEN (?) AND (?) AND Student_ID = (?)", (data_start, data_end, student_id))


    @classmethod
    def check_everyone_attendance(cls):
        return cls.query.all()


