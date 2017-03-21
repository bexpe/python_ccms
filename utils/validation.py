from utils.internal_validation import ValidateInternal
from utils.logging_form_validation_class import LoggingFormValidation
from utils.student_form_validation_class import  StudentFormValidation

class Validate:
    """
    Validates user input
    """

    @staticmethod
    def date_input(string):
        """
        Validate date input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    @staticmethod
    def student_id_input(string):
        """
        Validate student id input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    @staticmethod
    def team_input(string):
        """
        Validate team name input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    @staticmethod
    def grade_input(string):
        """
        Validate grade input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    @staticmethod
    def add_assignment_input(string):
        """
        Validate assignment input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    @staticmethod
    def submit_link_input(string):
        """
        Validate submit link input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    @staticmethod
    def edit_add_input(login, email, name, surname):
        """
        Validate edit/add form input
        :return: StudentFormValidation object
        """
        form_obj = StudentFormValidation(login, email, name, surname)

        form_obj.login = ValidateInternal.login_input(login)

        form_obj.email = ValidateInternal.email_input(email)

        form_obj.name = ValidateInternal.email_input(name)

        form_obj.surname = ValidateInternal.surname_input(surname)

        return form_obj

    @staticmethod
    def logging_input(login, password):
        """
        Validate logging input
        :return: LoggingFormValidation object
        """
        form_obj = LoggingFormValidation(login, password)

        form_obj.login = ValidateInternal.login_input(login)

        form_obj.password = ValidateInternal.password_input(password)

        return form_obj

