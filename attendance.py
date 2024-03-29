from users import Student
import csv


class Attendance:
    _attendance_list = []
    FILE = 'data/attendance.csv'

    def __init__(self, student_id, date, attendance):
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
        date = input('Insert date: ')
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
            cls._attendance_list.append(Attendance(student.id, date, attendance))
            cls.save_students_attendance_()
        else:
            print('Id is invalid')

    @classmethod
    def check_attendance_by_id(cls, student_id):
        """
        Creates students attendance list (id, day, attendance)
        :param student_id:
        :return: attendance by student: list
        """
        student_attendance_list = []
        student = Student.get_student_from_list_by_id(student_id)
        if student is not None:
            for attendance in cls._attendance_list:
                if attendance.student_id == student.id:
                    student_attendance_list.append(attendance)
            return student_attendance_list

    @classmethod
    def count_attendance_values(cls, student_id):
        """
        Counts student attendance
        :param student_id:
        :return: attendance: dictionary
        """
        values_attendance_by_id_dict = {'id': 0, 'day_sum': 0, 'present': 0, 'late': 0, 'absent': 0}
        attendance_list = cls.check_attendance_by_id(student_id)
        values_attendance_by_id_dict['id'] = student_id
        for attendance in attendance_list:
            values_attendance_by_id_dict['day_sum'] += 1
            if attendance.attendance == 'present':
                values_attendance_by_id_dict['present'] += 1
            elif attendance.attendance == 'late':
                values_attendance_by_id_dict['late'] += 1
            elif attendance.attendance == 'absent':
                values_attendance_by_id_dict['absent'] += 1
        return values_attendance_by_id_dict

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

    def objects_to_list(self):
        list_to_write = []

        for item in self._attendance_list:
            list_to_write.append(
                [item.student_id, item.date, item.attendance])
        return list_to_write

    @classmethod
    def save_students_attendance_(cls):
        table = cls.objects_to_list(cls)
        with open(cls.FILE, 'w') as file:
            for record in table:
                row = ','.join(record)
                file.write(row + "\n")

    @classmethod
    def load_students_attendance_(cls):
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')

            for line in reader:
                Attendance(line[0], line[1], line[2])
