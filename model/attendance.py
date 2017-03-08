from model.database import *


class Attendance:

    @staticmethod
    def get_student_attendance(student_id):
        db = Database()
        attendance = db.get("SELECT Date, Attendance_value FROM Attendance WHERE Student_ID=(?)", (student_id,))
        db.close()
        print(attendance)
        return attendance

    @staticmethod
    def set_attendance(student_id, attendance):
        db = Database()
        db.set("INSERT INTO Attendance Values (null,(?), date('now'), (?))", (student_id, attendance))
        db.close()

    @staticmethod
    def check_attendance(data_start, data_end, student_id):
        db = Database()
        check = db.get("SELECT * FROM Attendance WHERE Date BETWEEN (?) AND (?) AND Student_ID = (?)", (data_start, data_end, student_id))
        db.close()
        return check

    @staticmethod
    def check_everyone_attendance():
        db = Database()
        everyone = db.get("SELECT Attendance.Date, Student.Name, Student.Surname, Attendance.Attendance_value FROM Attendance INNER JOIN Student on Attendance.Student_ID = Student.ID")
        db.close()
        return everyone

Attendance.get_student_attendance(3)
