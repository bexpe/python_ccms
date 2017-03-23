from main import db


class Attendance(db.Model):

    # table name
    __tablename__ = 'attendance'

    # column name and stats
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
        """
        Remove attendance if exist
        """
        attendence = self.query.filter_by(student_id=self.student_id, date=self.date).first()
        if attendence:
            db.session.delete(attendence)
            db.session.commit()

    def save(self):
        """
        Save attendence, first checking if exist in date=today if exist remove this column
        """
        self.remove_attendance()
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_student_attendance(cls, student_id):
        """
        :param student_id: int(search student id)
        :return: attendance object
        """
        return cls.query.filter_by(student_id=student_id)

    @classmethod
    def check_attendance_by_date(cls, data_start, data_end, student_id):
        """
        :param data_start: start research data
        :param data_end: end of research data
        :param student_id: id of searching student
        :return: attendance object
        """
        return cls.query.filter_by(student_id=student_id).filter(cls.date.between(data_start, data_end)).order_by(cls.date)



    @classmethod
    def check_everyone_attendance(cls):
        """
        :return: everyone attendance object
        """
        return cls.query.all()


