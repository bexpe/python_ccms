import csv


class Assigments_Answer:
    """
    Class for students answer for current assigment.
    """

    def __init__(self, student_id, student_solution_link, grade):
        """
        Constructor
        params:
                student_id - string
                student_solution_link - string
        """
        self.student_id = student_id
        self.student_solution_link = student_solution_link
        self.grade = grade

    def grade_student_assigment(self, new_grade):
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
        return self.student_solution_link


class Assigment:
    """
    Class for assigment.
    """
    _assigments_list = []
    FILE = 'data/assigment.csv'

    def __init__(self, assigment_name, description):
        """
        params:
                assigment_name - string
                description - string
        """
        self.assigment_name = assigment_name
        self.description = description
        self.answers_list = []

        self._assigments_list.append(self)

    def get_assigment_name(self):
        """
        Method return current assigment name
        """
        return self.assigment_name

    def get_assigment_description(self):
        """
        Method return current assigment description
        """
        return self.description

    def get_assigment_answers(self):
        """
        Method return current assigment answers
        """
        return self.answers_list

    @classmethod
    def get_assigment_by_name(cls, assigment_to_find):
        """
        Method looks into class attribute _assigments_list to find assigment by given name.
        params:
                assigment_to_find - string
        """

        for assigment in cls._assigments_list:
            if assigment.get_assigment_name() == assigment_to_find:
                return assigment

    def submit_assigment_answer(self, student_id, student_answer, grade=None):
        """
        Students can give answer to current assigment.
        params:
                student_id - string
                student_answer - string
        """
        self.answers_list.append(Assigments_Answer(student_id, student_answer, grade))

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
        Method for find and return student grade for assigment
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
        answer.grade_student_assigment(new_grade)

    def remove_assigment(self):
        """
        Method remove current assigment from assigments list
        """
        self._assigments_list.remove(self)

    @classmethod
    def get_assigments_list(cls):
        """
        Method return class attribute _assigments_list with Assigments objects inside
        """
        return cls._assigments_list

    @classmethod
    def load_assigment_csv(cls):
        current_assigment = None

        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                if line[0] == "assigment":
                    current_assigment = Assigment(line[1], line[2])
                elif line[0] == "answer":
                    current_assigment.submit_assigment_answer(line[1], line[2], line[3])

    @classmethod
    def save_assigment_csv(cls):

        with open(cls.FILE, 'w') as file:
            for assigment in cls._assigments_list:
                row = "assigment,{},{}\n".format(assigment.get_assigment_name(), assigment.get_assigment_description())
                answers_list = assigment.get_assigment_answers()
                if answers_list:
                    for answer in answers_list:
                        row += "answer,{},{},{}\n".format(
                            answer.get_answer_student_id(),
                            answer.get_student_solution_link(),
                            answer.get_grade()
                        )
                file.write(row)
