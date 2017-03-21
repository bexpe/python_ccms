import re


class ValidateInternal:

    @staticmethod
    def empty(user_input):
        """
        Validate if user_input is empty
        :param user_input:
        :return: Boolean
        """
        if re.match(r'^\s*$', user_input):  # don't allow empty user_input or input with only white spaces
            return False
        return user_input

    @staticmethod
    def del_spaces(user_input):
        """
        Delete redundant spaces from sting
        :param user_input:
        :return: user_input/False
        """
        user_input = re.sub("\s\s+", " ", user_input)  # if its more than two spaces between words or at the beginning and
        # in the and of user_input, then they're changed for one space
        return user_input

    @staticmethod
    def del_script(user_input):
        if re.search(r'<script.*?>',
                     user_input):  # don't allow scripts in all user_input even between some different words
            return False
        return user_input

    @staticmethod
    def str_length(user_input):
        regex = re.compile("^.{1,150}$")  # allows from 1 to 150 letters in input
        if not regex.match(user_input):
            return False
        return user_input

    @staticmethod
    def initial_check(user_input):
        """
        Check if user_input is empty, delete spaces and del elements inside script tag
        :return: user_input/False
        """
        user_input = ValidateInternal.empty(user_input)
        user_input = ValidateInternal.del_spaces(user_input)
        user_input = ValidateInternal.del_script(user_input)
        user_input = ValidateInternal.str_length(user_input)

        return user_input

    @staticmethod
    def login_input(user_input):
        """
        Validate login input
        :return: user_input/False
        """
        user_input = ValidateInternal.initial_check(user_input)
        if user_input:
            if not re.match(r'^[A-Za-z0-9-]+(\.[a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', user_input):
                # lower and upper-case, dotes and numbers allowed before @, dotes and numbers allowed after @ but no upper-case!
                # after . not allowed upper- case in the end but .edu.com allowed!
                return False
            return user_input
        return False

    @staticmethod
    def email_input(user_input):
        """
        Validate email input
        :return: user_input/False
        """
        user_input = ValidateInternal.initial_check(user_input)
        if user_input:
            if not re.match(r'^[A-Za-z0-9-]+(\.[a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', user_input):
                # lower and upper-case, dotes and numbers allowed before @, dotes and numbers allowed after @ but no upper-case!
                # after . not allowed upper- case in the end but .edu.com allowed!
                return False
            return user_input
        return False

    @staticmethod
    def name_input(user_input):
        """
        Validate name input
        :return: user_input/False
        """
        user_input = ValidateInternal.initial_check(user_input)
        if user_input:
            regex = re.compile(r'(^[A-Z])+(-[^\W_]+)?([a-z]{2,})?(\-)([a-z]{2,})$', re.U)  # Upper-case at the beginning
            # required, one - allowed but without empty spaces!!! eg Catherine-Meg, no numbers allowed,
            # no upper-case at the end of a string allowed

            if not regex.match(user_input):
                return False
            return user_input
        return False

    @staticmethod
    def surname_input(user_input):
        """
        Validate surname input
        :return: user_input/False
        """
        user_input = ValidateInternal.initial_check(user_input)
        if user_input:
            regex = re.compile(r'(^[A-Z])+(-[^\W_]+)?([a-z]{2,})?(\-)([a-z]{2,})$', re.U)  # Upper-case at the beginning
            # required, one - allowed but without empty spaces!!! eg Catherine-Meg, no numbers allowed,
            # no upper-case at the end of a string allowed

            if not regex.match(user_input):
                return False
            return user_input
        return False

    @staticmethod
    def password_input(user_input):
        """
        Validate password
        :param user_input:
        :return: user_input/False
        """
        user_input = ValidateInternal.initial_check(user_input)
        if user_input:
            if re.match(r'[A-Za-z0-9@#$%^&+=]{4,}', user_input):  # all upper and lower case allowed with special
                # signs not shorter than 4 characters

                return user_input
        return False