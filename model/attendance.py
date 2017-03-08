from model.database import *


class Attendance:

    @staticmethod
    def get_student_attendance(student_id):
        db = Database()
        db.get("SELECT Attendance_value FROM Attendance WHERE Student_ID=(?)", (student_id,))
        db.close()

    @staticmethod
    def set_attendance(student_id, attendance):
        db = Database()
        db.set("INSERT INTO Attendance Values (null,(?), date('now'), (?))", (student_id, attendance))
        db.close()

    @staticmethod
    def check_attendance(data_start, data_end, student_id):
        db = Database()
        db.get("SELECT * FROM Attendance WHERE Date BETWEEN (?) AND (?) AND Student_ID = (?)", (data_start, data_end, student_id))
        db.close()

    @staticmethod
    def check_everyone_attendance():
        db = Database()
        db.get("SELECT * FROM Attendance")
