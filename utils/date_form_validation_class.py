class DateFormValidation:
    """
    Date form validation class.
    """
    def __init__(self, start_date, end_date, student_id):
        """
        Create data validation object.
        :param start_date:
        :param end_date:
        :param student_id:
        """
        self.start_date = start_date
        self.end_date = end_date
        self.student_id = student_id


    def valid_object(self):
        """
        When object is ready for database insert return True else False.
        :return: Boolean
        """
        if self.start_date != False and self.end_date != False and self.student_id != False:
            return True
        return False
