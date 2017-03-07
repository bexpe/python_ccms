from model.database import *


class Attendance:

    def __init__(self):
        self.db = Database()

    def student_attendance(self, student_id):
        z = self.db.get("SELECT Attendance_value FROM Attendance WHERE Student_ID=(?)", (student_id))
        print(z)


z = Attendance()
z.student_attendance(1)
