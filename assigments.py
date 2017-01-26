class Assigments_answer:
	"""
	Class for students answer for current assigment.
	"""

    def __init__(self, student_id, student_answer):
    	"""
		Constructor
		params:
			student_id - string
			student_answer - string
    	"""
    	self.student_id = student_id
    	self.student_answer = student_answer
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


class Assigment:
	"""
	Class for assigment.
	"""
	_assigments_list = []

    def __init__(self, assigment_name, description):
    	"""
		params:
			assigment_name - string
			description - string
    	"""
    	self.assigment_name = assigment_name
    	self.description = description
    	self.answers_list = []

    def get_assigment_name(self):
    	"""
    	Method return current assigment name
    	"""
    	return self.assigment_name

    def get_assigment_by_name(self, assigment_to_find):
    	"""
    	Method looks into class attribute _assigments_list to find assigment by given name.
    	params:
    		assigment_to_find - string
    	"""

    	for assigment in _assigments_list:
    		if assigment.get_assigment_name() == assigment_to_find:
    			return assigment

    def submit_assigment_answer(self, student_id, student_answer):
    	"""
		Students can give answer to current assigment.
		params:
			student_id - string
			student_answer - string
    	"""
    	self.answers_list.append(Assigments_answer(student_id, student_answer))

    def get_student_answer(self, student_id):
    	"""
		Method looks in current assigmet answers_list to find student answer by his given id
		params:
			student_id - string
    	"""
    	for answer in self.answers_list;
    		if answer.get_answer_student_id() == student_id:
    			return answer

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
    	return _assigments_list
