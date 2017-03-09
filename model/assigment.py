from model.database import Database


class Assigment:

    def __init__(self, id, name, task_type, answers):
        self.id = id
        self.name = name
        self.task_type = task_type
        self.answers = answers

    def get_student_answer(self, student_id):
        for answer in self.answers:
            if answer.student_id == student_id:
                return answer

    def get_team_answer(self, team_id):
        for answer in self.answers:
            if answer.team_id == team_id:
                return answer

    @staticmethod
    def get_assigment_by_id(task_id):
        db = Database()
        assigment_data = db.get("SELECT * FROM Assignments WHERE id=(?)", (task_id,))[0]
        answers = db.get("SELECT * FROM Answers WHERE Assignment_ID=(?)",
                         (assigment_data[0],))  # get answers for assigment with a[0]-id
        answers = [Answer(d[0], d[1], d[2], d[3], d[4], d[5], d[6]) for d in answers]
        assigment_object = Assigment(assigment_data[0], assigment_data[1], assigment_data[2], answers)
        return assigment_object
        db.close()

    @staticmethod
    def add_new_assigment(name, task_type):
        db = Database()
        db.set("INSERT INTO Assignments(name, task_type) VALUES (?,?)", (name, task_type))
        db.close()

    @staticmethod
    def get_list_of_assigments():
        db = Database()
        assigments_data_list = db.get("SELECT * FROM Assignments")
        assigments_objects_list = []
        for a in assigments_data_list:
            answers = db.get("SELECT * FROM Answers WHERE Assignment_ID=(?)",
                             (a[0],))  # get answers for assigment with a[0]-id
            answers = [Answer(d[0], d[1], d[2], d[3], d[4], d[5], d[6]) for d in answers]
            assigments_objects_list.append(Assigment(a[0], a[1], a[2], answers))
        return assigments_objects_list
        db.close()


class Answer:

    def __init__(self, id, answer_text, grade, student_id, team_id, assigment_id, grade_date):
        self.id = id
        self.answer_text = answer_text
        self.grade = grade
        self.student_id = student_id
        self.team_id = team_id
        self.assigment_id = assigment_id
        self.grade_date = grade_date

    @classmethod
    def submit_personal_answer(cls, answer_text, student_id, assigment_id):
        db = Database()
        is_answer_exist = db.get(
            "SELECT EXISTS (SELECT * FROM Answers WHERE Student_ID=(?) AND Assignment_ID=(?))", (student_id, assigment_id))
        if is_answer_exist[0][0]:
            db.set("UPDATE Answers SET Answer_text=(?) WHERE Student_ID=(?) AND Assignment_ID=(?)",
                   (answer_text, student_id, assigment_id))
        else:
            db.set("INSERT INTO Answers(Answer_text, Student_ID, Assignment_ID) VALUES (?,?,?)",
                   (answer_text, student_id, assigment_id))
        db.close()

    @classmethod
    def submit_team_answer(cls, answer_text, student_id, assigment_id):
        db = Database()
        # get student by id
        team_id = db.get("SELECT Team_ID FROM Student WHERE id=(?)", (student_id,))[0][0]
        is_answer_exist = db.get(
            "SELECT EXISTS (SELECT * FROM Answers WHERE Team_ID=(?) AND Assignment_ID=(?))", (team_id, assigment_id))
        if is_answer_exist[0][0]:
            db.set("UPDATE Answers SET Answer_text=(?) WHERE Team_ID=(?) AND Assignment_ID=(?)",
                   (answer_text, team_id, assigment_id))
        else:
            db.set("INSERT INTO Answers(Answer_text, Team_ID, Assignment_ID) VALUES (?,?,?)",
                   (answer_text, team_id, assigment_id))
        db.close()

    @classmethod
    def submit_answer(cls, answer_text, student_id, assigment_id):
        db = Database()
        task_type = db.get("SELECT Task_type FROM Assignments WHERE id=(?)", (assigment_id,))[0][0]
        if task_type == "Personal":
            cls.submit_personal_answer(answer_text, student_id, assigment_id)
        elif task_type == "Team":
            cls.submit_team_answer(answer_text, student_id, assigment_id)
        db.close()

    def grade_answer(self, new_grade):
        self.grade = new_grade
