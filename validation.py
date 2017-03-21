class Validate:
    """
    Validates user input
    """

    def is_empty(self, string):
        """
        Validate if string is empty
        :param string:
        :return: Boolean
        """
        #TODO return True if is empty, else return False
        pass

    def del_spaces(self, string):
        """
        Delete redundant spaces from sting
        :param string:
        :return: string/False
        """
        #TODO: del spaces
        pass

    def del_script(self, string):
        pass

    def initial_check(self, string):
        """
        Check if string is empty, delete spaces and del elements inside script tag
        :return: String/False
        """
        validate = Validate()
        if validate.is_empty(string):
            return False
        validated_str = validate.del_spaces(string)
        validated_str = validate.del_script(validated_str)

        return  validated_str

    @staticmethod
    def date_input(string):
        """
        Validate date input
        :return: string/False
        """
        validate = Validate()
        validated_str = validate.initial_check(string)
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
        validate = Validate()
        validated_str = validate.initial_check(string)
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
        validate = Validate()
        validated_str = validate.initial_check(string)
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
        validate = Validate()
        validated_str = validate.initial_check(string)
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
        validate = Validate()
        validated_str = validate.initial_check(string)
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
        validate = Validate()
        validated_str = validate.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    @staticmethod
    def edit_add_input(login, email, name, surname):
        """
        Validate edit/add form input
        :return: string/False
        """
        edit_add_list = []
        validate = Validate()

        validated_login = validate.login_input(login)
        edit_add_list.append(validated_login)

        validated_email = validate.email_input(email)
        edit_add_list.append(validated_email)

        validated_name = validate.email_input(name)
        edit_add_list.append(validated_name)

        validated_surname = validate.surname_input(surname)
        edit_add_list.append(validated_surname)

        return edit_add_list

    @staticmethod
    def logging_input(login, password):
        """
        Validate logging input
        :return: list(strings)/list(False)
        """
        logging_list = []
        validate = Validate()

        validated_login = validate.login_input(login)
        logging_list.append(validated_login)

        validated_password = validate.password_input(password)
        logging_list.append(validated_password)

        return logging_list

    def login_input(self, string):
        """
        Validate login input
        :return: string/False
        """
        validate = Validate()
        validated_str = validate.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    def email_input(self, string):
        """
        Validate email input
        :return: string/False
        """
        validate = Validate()
        validated_str = validate.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    def name_input(self, string):
        """
        Validate name input
        :return: string/False
        """
        validate = Validate()
        validated_str = validate.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    def surname_input(self, string):
        """
        Validate surname input
        :return: string/False
        """
        validate = Validate()
        validated_str = validate.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False


    def password_input(self, string):
        """
        Validate password
        :param string:
        :return: string/False
        """
        validate = Validate()
        validated_str = validate.initial_check(string)
        if validated_str:
            #TODO: YOUR CODE GOES HERE
            return validated_str
        return False
