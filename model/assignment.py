from main import db


class Assignment(db.Model):

    __tablename__ = 'Assignments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    task_type = db.Column(db.String)

    def __init__(self, name, task_type):
        self.name = name
        self.task_type = task_type

    def get_student_answer(self, student_id):
        return Answer.query.filter_by(student_id=student_id, assignment_id=self.id).first()

    def get_team_answer(self, team_id):
        return Answer.query.filter_by(team_id=team_id, assignment_id=self.id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_assignment_by_id(cls, task_id):
        return cls.query.get(task_id)

    @classmethod
    def get_list_of_assignments(cls):
        return cls.query.all()


class Answer(db.Model):

    __tablename__ = 'Answers'
    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String)
    grade = db.Column(db.String)
    student_id = db.Column(db.Integer)
    team_id = db.Column(db.Integer)
    assignment_id = db.Column(db.Integer)
    grade_date = db.Column(db.String)

    def __init__(self, answer_text, assignment_id, grade=None, grade_date=None, student_id=None, team_id=None):
        self.answer_text = answer_text
        self.grade = grade
        self.student_id = student_id
        self.team_id = team_id
        self.assignment_id = assignment_id
        self.grade_date = grade_date

    @classmethod
    def get_answer_by_id(cls, answer_id):
        return cls.query.get(answer_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()