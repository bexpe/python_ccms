from utils.abstract_form_validation import FormValidation

class LoggingFormValidation(FormValidation):
    """
    Logging form validation class.
    """
    def __init__(self, login, password):
        """
        Create class object
        :param login:
        :param password:
        """
        self.login = login
        self.password = password

    def valid_object(self):
        """
        When object is ready for database insert return True else False.
        :return: Boolean
        """
        if self.login != False and self.password != False:
            return True
        return False
