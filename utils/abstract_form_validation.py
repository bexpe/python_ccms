from abc import ABCMeta

class FormValidation(metaclass=ABCMeta):
    """
    Abstract class for form validation
    """

    def valid_object(self):
        """
        When object is ready for database insert return True else False.
        :return: Boolean
        """
        pass