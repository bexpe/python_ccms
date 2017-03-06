import sqlite3


class AssignmentAnswerModel:
    """
    Connects Assignment Class to database.
    """
    def __init__(self):
        self.connect = sqlite3.connect("todo.db")
        self.cur = self.connect.cursor()


    def set_assignment_answer_obj(self,student_solution_link, grade, student_id, assignment_id):
        """
        Add answer object to database.
        :param student_solution_link:
        :param grade:
        :param student_id:
        :param assignment_id:
        :return: None
        """
        try:
            self.cur.execute("INSERT INTO Answers(Answer_text,Grade,Student_ID,Assignment_id) VALUES(?,?,?,?)",
                            (student_solution_link, grade, student_id, assignment_id))
            self.connect.commit()

        except sqlite3.OperationalError as err:
            print("Cant add/edit this {}".format(err))

        except sqlite3.Error as err:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base {}') .format(err)


    def get_assignment_answer_obj(self,student_id, assignment_id):
        """
        DB sample output [(2, 'Circle is round', 5, 1, 2)] : as in Constructor of AssignmentAnswer body
        :param student_id:
        :param assignment_id:
        :return:
        """

        try:
            self.cur.execute("SELECT * FROM Answers WHERE Student_ID=(?) AND Assignment_id=(?)",
                        (student_id, assignment_id))
            self.connect.commit()

        except sqlite3.OperationalError as err:
            print("Cant add/edit this {}".format(err))

        except sqlite3.Error as err:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base {}') .format(err)

    def update_assignment_answer_obj(self, answer_id, student_solution_link, grade, student_id, assignment_id):
        """
        Update answer object in database.
        :param answer_id:
        :param student_solution_link:
        :param grade:
        :param student_id:
        :param assignment_id:
        :return:
        """

        try:
            self.cur.execute("UPDATE Answers SET Answer_text=(?), Grade=(?), Student_ID=(?), Assignment_id=(?) WHERE ID=(?)",
                        (student_solution_link, grade, student_id, assignment_id, answer_id))
            self.connect.commit()

        except sqlite3.OperationalError as err:
            print("Cant add/edit this {}".format(err))

        except sqlite3.Error as err:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base {}') .format(err)
