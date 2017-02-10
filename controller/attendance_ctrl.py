import sqlite3
import datetime
from controller.student_ctrl import Student
from model.attendance_model import AttendanceModel


class Attendance:
    _attendance_list = []
    FILE = 'data/attendance.csv'

    def __init__(self, student_id, date, attendance, attendance_id=None):
        self.attendance_id = attendance_id
        self.student_id = student_id
        self.date = date
        self.attendance = attendance

    @classmethod
    def set_attendance(cls):
        """
        Creates attendance object with (id, day, attendance), and saves list to csv
        :return: None
        """
        student_id = input('Insert student id: ')
        date = datetime.datetime.now().date()
        option = input('A= present, B= late C= not there: ')
        option = option.upper()
        if option == 'A':
            attendance = 'present'
        elif option == 'B':
            attendance = 'late'
        elif option == 'C':
            attendance = 'absent'
        else:
            print("There is no such option.")
            return None
        student = Student.get_student_from_list_by_id(student_id)
        if student is not None:
            new_attendance = Attendance(int(student_id), date, attendance)
            try:
                AttendanceModel.add_attendance_to_db(new_attendance)
            except sqlite3.IntegrityError:
                print('Invalid data')
        else:
            print('Id is invalid')

    @classmethod
    def check_attendance_by_id(cls, student_id):
        """
        Creates students attendance list (id, day, attendance)
        :param student_id:
        :return: attendance by student: list
        """

        student = Student.get_student_from_list_by_id(student_id)
        if student is not None:
            student_attendance_list = AttendanceModel.db_get_attendance_by_id(student_id)
            return student_attendance_list

    @classmethod
    def count_attendance_values(cls, student_id):
        """
        Counts student attendance
        :param student_id:
        :return: attendance: dictionary
        """
        count_attendance_dict = {'id': 0, 'day_sum': 0, 'present': 0, 'late': 0, 'absent': 0}
        values = AttendanceModel.db_get_count_attendance_values(student_id)
        if values:
            for item in values:
                count_attendance_dict[item[0]] = item[1]
                count_attendance_dict['day_sum'] = AttendanceModel.db_get_attendance_values_sum(student_id)[0][0]
        count_attendance_dict['id'] = student_id
        return count_attendance_dict

    @classmethod
    def print_attendance_percentage(cls):
        """
        Prints percentage attendance dictionary
        :return: None
        """
        student_id = input('Insert student id \n')
        student_id = Student.get_student_from_list_by_id(student_id)
        if student_id is not None:
            attendance_dict = cls.count_attendance_values(student_id.id)
            if attendance_dict['day_sum'] == 0:
                print('There is no attendance record for student: {}' .format(student_id.id))
            else:
                for key, value in attendance_dict.items():
                    if value is not student_id.id:
                        percentage = 100 * int(value) // attendance_dict['day_sum']
                        if key is not 'id' and key is not 'day_sum':
                            print('{} : {} [day] = {} %'.format(key, value, percentage))
        else:
            print('Id is invalid')


Attendance.set_attendance()
Attendance.count_attendance_values(1)
Attendance.count_attendance_values(1)
Attendance.count_attendance_values(str(1))