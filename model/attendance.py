from model.database import *


class Attendance:

    def __init__(self):
        self.db = Database()

    def student_attendance(self, student_id):
        z = self.db.get("SELECT Attendance_value FROM Attendance WHERE Student_ID=(?)", (student_id,))

        print(z)

    def set_attendance(self, student_id, attendance):
        x = self.db.set("INSERT INTO Attendance Values (null,(?), date('now'), (?))", (student_id, attendance))

    def check_attendance(self, data_start, data_end):
        xx = self.db.get("SELECT * FROM Attendance WHERE Date BETWEEN (?) AND (?)", (data_start, data_end))
        print(xx)

z = Attendance()
z.student_attendance(1)

