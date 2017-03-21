class ValidateInternal:

    @staticmethod
    def is_empty(string):
        """
        Validate if string is empty
        :param string:
        :return: Boolean
        """
        # TODO return True if is empty, else return False
        pass

    @staticmethod
    def del_spaces(string):
        """
        Delete redundant spaces from sting
        :param string:
        :return: string/False
        """
        # TODO: del spaces
        pass

    @staticmethod
    def del_script(string):
        pass

    @staticmethod
    def initial_check(string):
        """
        Check if string is empty, delete spaces and del elements inside script tag
        :return: String/False
        """
        if ValidateInternal.is_empty(string):
            return False
        validated_str = ValidateInternal.del_spaces(string)
        validated_str = ValidateInternal.del_script(validated_str)

        return validated_str

    @staticmethod
    def login_input(string):
        """
        Validate login input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            # TODO: YOUR CODE GOES HERE
            return validated_str
        return False

    @staticmethod
    def email_input(string):
        """
        Validate email input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            # TODO: YOUR CODE GOES HERE
            return validated_str
        return False

    @staticmethod
    def name_input(string):
        """
        Validate name input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            # TODO: YOUR CODE GOES HERE
            return validated_str
        return False

    @staticmethod
    def surname_input(string):
        """
        Validate surname input
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            # TODO: YOUR CODE GOES HERE
            return validated_str
        return False

    @staticmethod
    def password_input(string):
        """
        Validate password
        :param string:
        :return: string/False
        """
        validated_str = ValidateInternal.initial_check(string)
        if validated_str:
            # TODO: YOUR CODE GOES HERE
            return validated_str
        return False