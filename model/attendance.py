from model.database import *
from main import db
from datetime import *
import time


class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    date = db.Column(db.String)
    attendance_value = db.Column(db.String)

    def __init__(self, attendance_id, student_id=None, date=None, attendance_value=None):
        self.student_id = student_id
        self.attendance_value = attendance_value
        self.attendance_id = attendance_id
        self.date = date

    def remove_attendance(self):
        attendence = self.query.filter_by(student_id=self.student_id, date=self.date).first()
        if attendence:
            db.session.delete(attendence)
            db.session.commit()

    def save(self):
        self.remove_attendance()
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_student_attendance(cls, student_id):
        return cls.query.filter_by(student_id=student_id)

    @classmethod
    def check_attendance_by_date(cls, data_start, data_end, student_id):
        return cls.query.filter_by(student_id=student_id)
        # ("SELECT Date, Attendance_value FROM Attendance WHERE Date BETWEEN (?) AND (?) AND Student_ID = (?)", (data_start, data_end, student_id))


    @classmethod
    def check_everyone_attendance(cls):
        return cls.query.all()


