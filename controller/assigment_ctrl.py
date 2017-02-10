from assignment_model import AssignmentAnswerModel


class AssignmentAnswer:
    """
    Class for students answer for current assignment.
    """

    def __init__(self, student_solution_link, student_id, assignment_id,
                 answer_id=None, grade=None):
        """
        Constructor
        params:
                student_id - string
                student_solution_link - string
        """
        self.answer_id = answer_id
        self.student_solution_link = student_solution_link
        self.grade = grade
        self.student_id = student_id
        self.assignment_id = assignment_id

    def get_answer_id(self):
        """
        Get answer id
        :return:
        """
        return self.answer_id

    def grade_student_assignment(self, new_grade):
        """
        Method for grade student answer
        params:
                new_grade - int
        """
        self.grade = new_grade

    def get_grade(self):
        """
        Method return student answer grade
        """
        return self.grade

    def get_answer_student_id(self):
        """
        Method return student_id for current answer
        """
        return self.student_id

    def get_student_solution_link(self):
        """
        Gets student_solution_link as string Answer object
        :return: student_solution_link as string
        """
        return self.student_solution_link

    def get_assignment_id(self):
        """
        Gets assignment_id as string from Answer object
        :return: assignment_id as string
        """
        return self.assignment_id

    @classmethod
    def set_assignment_answer(cls, student_solution_link, student_id, assignment_id):
        """
        Creates object of answer not yet graded, and sends it to database.
        :param student_solution_link:
        :param student_id:
        :param assignment_id:
        :return: None
        """
        answer = AssignmentAnswer(student_solution_link, student_id, assignment_id)

        AssignmentAnswerModel.set_assignment_answer_obj(answer.get_student_solution_link(),
                                                        answer.get_grade(),
                                                        answer.get_answer_student_id(),
                                                        answer.get_assignment_id())

    @classmethod
    def get_assignment_answer(cls, student_id, assignment_id):
        """
        Gets answer object from database and creates it.
        :param student_id:
        :param assignment_id:
        :return: answer_object
        """
        answer_db = AssignmentAnswerModel.get_assignment_answer_obj(student_id, assignment_id)

        answer_object = AssignmentAnswer(answer_db[0][1],
                                         answer_db[0][3],
                                         answer_db[0][4],
                                         answer_db[0][0],
                                         answer_db[0][2])
        return answer_object

    @classmethod
    def set_grade(cls, grade, student_id, assignment_id):
        """Set student grade"""
        answer = AssignmentAnswer.get_assignment_answer(student_id, assignment_id)

        AssignmentAnswerModel.update_assignment_answer_obj(answer.get_answer_id(),
                                                           answer.get_student_solution_link(),
                                                           grade,
                                                           answer.get_answer_student_id(),
                                                           answer.get_assignment_id())


class Assignment:
    """
    Class for assignment.
    """
    _assignments_list = []
    FILE = 'data/assignment.csv'

    def __init__(self, assignment_name, description):
        """
        params:
                assignment_name - string
                description - string
        """
        self.assignment_name = assignment_name
        self.description = description

    def get_assignment_name(self):
        """
        Method return current assignment name
        """
        return self.assignment_name

    def get_assignment_description(self):
        """
        Method return current assignment description
        """
        return self.description

    def get_assignment_answers(self):
        """
        Method return current assignment answers
        """
        return self.answers_list

    @classmethod
    def get_assignment_by_name(cls, assignment_to_find):
        """
        Method looks into class attribute _assignments_list to find assignment by given name.
        params:
                assignment_to_find - string
        """

        for assignment in cls._assignments_list:
            if assignment.get_assignment_name() == assignment_to_find:
                return assignment

    def submit_assignment_answer(self, student_id, student_answer, grade=None):
        """
        Students can give answer to current assignment.
        params:
                student_id - string
                student_answer - string
        """
        self.answers_list.append(AssignmentAnswer(student_id, student_answer, grade))

    def get_student_answer(self, student_id):
        """
        Method looks in current assignment answers_list to find student answer by his given id
        params:
                student_id - string
        """
        for answer in self.answers_list:
            if answer.get_answer_student_id() == student_id:
                return answer

    def get_student_grade(self, student_id):
        """
        Method for find and return student grade for assignment
        params:
                student_id - string
        """
        answer = self.get_student_answer(student_id)
        if answer:
            return answer.get_grade()

    def get_student_solution_link(self, student_id):
        answer = self.get_student_answer(student_id)
        return answer.get_student_solution_link()

    def grade_student_answer(self, student_id, new_grade):
        answer = self.get_student_answer(student_id)
        answer.grade_student_assignment(new_grade)

    def remove_assignment(self):
        """
        Method remove current assignment from assignments list
        """
        self._assignments_list.remove(self)

    @classmethod
    def get_assignments_list(cls):
        """
        Method return class attribute _assignments_list with Assignments objects inside
        """
        return cls._assignments_list

