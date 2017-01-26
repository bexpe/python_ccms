import csv

class Assigments_Answer:

    """
    Class for students answer for current assigment.
    """

    def __init__(self, student_id, student_solution_link):
        """
        Constructor
        params:
                student_id - string
                student_solution_link - string
        """
        self.student_id = student_id
        self.student_solution_link = student_solution_link
        self.grade = None

    def grade_student_assigment(self, new_grade):
        """
        Method for grade student answer
        params:
                new_grade - int
        """
        self.grade = new_grade

    def get_student_grade(self):
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

    def submit_assigment_answer(self, student_id, student_answer):
        """
        Students can give answer to current assigment.
        params:
                student_id - string
                student_answer - string
        """
        self.answers_list.append(Assigments_Answer(student_id, student_answer))

    def get_student_answer(self, student_id):
        """
        Method looks in current assigmet answers_list to find student answer by his given id
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
        return answer.get_student_grade()

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

    def objects_to_list(self):
        assignments = []

        for assignment in self._assigments_list:
            assignments.append([assignment.assigment_name, assignment.description])
        return assignments

    @classmethod
    def load_assigment_csv(cls):
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:Assigment(line[0], line[1])

    @classmethod
    def save_assigment_csv(cls):
        table = cls.objects_to_list(cls)
        with open(cls.FILE, 'w') as file:
            for record in table:
                row = ','.join(record)
                file.write(row + "\n")

