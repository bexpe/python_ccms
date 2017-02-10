import sqlite3


class AttendanceModel:
    """
    MCV Model class for attendance, connection to database.
    """
    @staticmethod
    def add_attendance_to_db(attendance_object):
        try:
            connect = sqlite3.connect('baza_danych.db')
            cur = connect.cursor()
            cur.execute("INSERT INTO Student_Attendance(Student_id, Date, Attendance_value) VALUES(?,?,?)",
                        (attendance_object.student_id, attendance_object.date, attendance_object.attendance))
            connect.commit()
        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()

    @staticmethod
    def db_get_attendance_by_id(student_id):
        """
        Get attendance list by student id.
        :param student_id:
        :return: attendance_list_by_student
        """
        try:
            connect = sqlite3.connect('baza_danych.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
            cur = connect.cursor()
            cur.execute("SELECT Attendance_value, Date FROM Student_Attendance WHERE Student_id = (?)", str(student_id))
            connect.commit()
            attendance_list_by_student = cur.fetchall()
            return attendance_list_by_student

        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()

    @staticmethod
    def db_get_count_attendance_values(student_id):
        """
        Get from database counted attendance values by id.
        :param student_id:
        :return: counted_attendance_values (object)
        """
        try:
            connect = sqlite3.connect('baza_danych.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
            cur = connect.cursor()
            cur.execute("SELECT Attendance_value, COUNT(Attendance_value) from Student_Attendance "
                        "WHERE Student_id = (?)"
                        "GROUP BY Attendance_value ORDER BY Attendance_value ASC;", str(student_id))
            connect.commit()
            counted_attendance_values = cur.fetchall()
            return counted_attendance_values
        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()

    @staticmethod
    def db_get_attendance_values_sum(student_id):
        """
        get_attendance_values_sum
        :param student_id:
        :return: attendance_by_student_id_sum
        """
        try:
            connect = sqlite3.connect('baza_danych.db')
            cur = connect.cursor()
            cur.execute("SELECT count(Attendance_value) as 'sum_attendance' from Student_Attendance "
                        "where student_id = (?)", str(student_id))
            connect.commit()
            attendance_by_student_id_sum = cur.fetchall()
            return attendance_by_student_id_sum
        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()
