from database import Database


class Assigment:
    def __init__(self, id, name, task_type, answers):
        self.id = id
        self.name = name
        self.task_type = task_type
        self.grades = grades
        self.answers = answers

    def submit_assigment():
        pass

    def add_new_assigment():
        pass

    def grade_student_answer():
        pass

    def get_student_grade():
        pass

    def get_student_answer():
        pass

    @staticmethod
    def get_list_of_assigments():
        db = Database()
        assigments_data_list = db.get("SELECT * FROM Assignments")
        assigments_objects_list = []
        for a in assigments_data_list:
            answers = db.get("SELECT * FROM Answers WHERE Assigment_ID=(?)", (a[0]))
            answers = [Answer(d[0], d[1], d[2], d[3], d[4], d[5]) for d in answers]
            assigments_objects_list.append(Assigment(a[0],a[1],a[2], answers))
        return assigments_objects_list
        db.close()

    def get_assigment_details():
        pass


class Answer:
    def __init__(self, id, answer_text, grade, student_id, assigment_id, grade_date):
        self.id = id
        self.answer_text = answer_text
        self.grade = grade
        self.student_id = student_id
        self.assigment_id = assigment_id
        self.grade_date = grade_date