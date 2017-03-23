from utils.internal_validation import ValidateInternal
from utils.logging_form_validation_class import LoggingFormValidation
from utils.student_form_validation_class import StudentFormValidation
from utils.date_form_validation_class import DateFormValidation
import re


class Validate:
    """
    Validates user input
    """

    @staticmethod
    def date_validation(start_date, end_date, student_id):
        """
        Validate date input
        :return: string/False
        """
        start_date = ValidateInternal.date_input(start_date)
        end_date = ValidateInternal.date_input(end_date)
        student_id = Validate.student_id_input(student_id)
        form_obj = DateFormValidation(start_date, end_date, student_id)

        return form_obj

    @staticmethod
    def student_id_input(string):
        """
        Validate student id input
        :return: string/False
        """
        user_input = ValidateInternal.initial_check(string)
        if type(user_input) is str:
            if re.match(r'^[0-9]+$', user_input):  # all number, at least one
                return user_input
        return False

    @staticmethod
    def team_input(string):
        """
        Validate team name input
        :return: string/False
        """
        user_input = ValidateInternal.initial_check(string)
        if type(user_input) is str:
            if re.match(r'[A-Za-z0-9@#$%^&+=]+', user_input):  # all upper and lower case allowed with special
                # signs not shorter than 1 character
                return user_input
        return False

    @staticmethod
    def grade_input(string):
        """
        Validate grade input
        :return: string/False
        """
        user_input = ValidateInternal.initial_check(string)
        if type(user_input) is str:
            if re.match(r'^[0-9]{1,3}$', user_input):  # allows numbers, only 1-3 digits
                return user_input
        return False

    @staticmethod
    def add_assignment_input(string):
        """
        Validate assignment input
        :return: string/False
        """
        user_input = ValidateInternal.initial_check(string)
        if type(user_input) is str:
            if re.match(r'[A-Za-z0-9@#$%^&+=]+', user_input):  # all upper and lower case allowed with special
                # signs not shorter than 1 character

                return user_input
        return False

    @staticmethod
    def submit_link_input(string):
        """
        Validate submit link input
        :return: string/False
        """
        user_input = ValidateInternal.initial_check(string)
        if type(user_input) is str:
            if user_input.startswith('http'):
                if not re.match(r'^(http|https)://(.+)\.(.+)',
                                user_input):  # looking for http/s on the beginning with // and:
                    return False

                k = re.match(r'^(http|https)://(.+)\.(.+)', user_input)  # assigning to variable k this matching regex
                link_name = 'assignment_link'
                user_input = re.sub(r'^(http|https)://(.+)\.(.+)', '<a href = "' + k.string + '">' + link_name + '</a>',
                                    user_input)  # swapping a link for a html url with href
                return user_input

            elif user_input.startswith('www'):
                if not re.match(r'^www.(.+)\.(.+)$', user_input):  # looking for www. on the beginning
                    return False

                k = re.match(r'^www.(.+)\.(.+)$', user_input)  # assigning to variable
                link_name = 'assignment_link'
                user_input = re.sub(r'^www.(.*)\.(.*)', '<a href = "http://' + k.group(1) + '.' + k.group(2) + '">' +
                                    link_name + '</a>', user_input)
                return user_input
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

        form_obj.name = ValidateInternal.name_input(name)

        form_obj.surname = ValidateInternal.surname_input(surname)

        return form_obj

    @staticmethod
    def is_form_obj_valid(form_object):
        StudentFormValidation.valid_object(form_object)

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
