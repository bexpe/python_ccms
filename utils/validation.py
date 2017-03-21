from internal_validation import ValidateInternal
from logging_form_validation_class import LoggingFormValidation
from student_form_validation_class import  StudentFormValidation
import re

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
        user_input = ValidateInternal.initial_check(string)
        if user_input:
            #TODO: YOUR CODE GOES HERE
            return user_input
        return False


    @staticmethod
    def student_id_input(string):
        """
        Validate student id input
        :return: string/False
        """
        user_input = ValidateInternal.initial_check(string)
        if user_input:
            #TODO: YOUR CODE GOES HERE
            return user_input
        return False


    @staticmethod
    def team_input(string):
        """
        Validate team name input
        :return: string/False
        """
        user_input = ValidateInternal.initial_check(string)
        if user_input:
            if re.match(r'[A-Za-z0-9@#$%^&+=]{1,}', user_input):  # all upper and lower case allowed with special
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
        if user_input:
            #TODO: YOUR CODE GOES HERE
            return user_input
        return False


    @staticmethod
    def add_assignment_input(string):
        """
        Validate assignment input
        :return: string/False
        """
        user_input = ValidateInternal.initial_check(string)
        if user_input:
            if re.match(r'[A-Za-z0-9@#$%^&+=]{1,}', user_input):  # all upper and lower case allowed with special
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
        if user_input:
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
