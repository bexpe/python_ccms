class User:

    def __init__(self, name, surname, email, date_of_birth, city, phone):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.city = city
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        """
        This method gets an users email
        :return: users email as an object
        """
        return "{} {}".format(self.name, self.surname)

    def get_password(self):
        """
        This method gets an users password.
        :return: users password as an object
        """
        return self.password
