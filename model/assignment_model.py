import sqlite3

class AssignmentAnswerModel:
    """
    Connects Assignment Class to database.
    """
    @staticmethod
    def set_assignment_answer_obj(student_solution_link, grade, student_id, assignment_id):
        """

        :param student_solution_link:
        :param grade:
        :param student_id:
        :param assignment_id:
        :return: None
        """
        try:
            connect = sqlite3.connect('db.db')
            cur = connect.cursor()
            cur.execute("INSERT INTO Answers(Answer_text,Grade,Student_ID,Assignment_id) VALUES(?,?,?,?)",
                        (student_solution_link, grade, student_id, assignment_id))
            connect.commit()
        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()

    @staticmethod
    def get_assignment_answer_obj(student_id, assignment_id):
        """
        DB sample output [(2, 'Circle is round', 5, 1, 2)] : as in Constructor of AssignmentAnswer body
        :param student_id:
        :param assignment_id:
        :return:
        """
        try:
            connect = sqlite3.connect('db.db')
            cur = connect.cursor()
            cur.execute("SELECT * FROM Answers WHERE Student_ID=(?) AND Assignment_id=(?)",
                        (student_id, assignment_id))
            connect.commit()
            answer = cur.fetchall()
            return answer
        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()

    @staticmethod
    def update_assignment_answer_obj(answer_id, student_solution_link, grade, student_id, assignment_id):
        try:
            connect = sqlite3.connect('db.db')
            cur = connect.cursor()
            cur.execute("UPDATE Answers SET Answer_text=(?), Grade=(?), Student_ID=(?), Assignment_id=(?) WHERE ID=(?)",
                        (student_solution_link, grade, student_id, assignment_id, answer_id))
            connect.commit()
            answer = cur.fetchall()
            return answer
        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()
