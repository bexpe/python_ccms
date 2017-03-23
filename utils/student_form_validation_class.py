class StudentFormValidation:
    """
        Student form validation class.

    """
    def __init__(self, user_id, login, email, name, surname):
        """
        create class object
        :param login:
        :param email:
        :param name:
        :param surname:
        """
        self.user_id = user_id
        self.login = login
        self.email = email
        self.name = name
        self.surname = surname

    def valid_object(self):
        """
        When object is ready for database insert return True else False.
        :return: Boolean
        """
        if self.login != False and self.email != False and self.name != False and self.surname != False:
            return True
        return False