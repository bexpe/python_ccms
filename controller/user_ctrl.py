from model.user_model import User_model


class User:

    def __init__(self, name, surname, email, date_of_birth, city, phone, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
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

    def edit_user(self, name, surname, email, date_of_birth, city, phone):
        current_name = self.get_full_name()
        data_to_change = [name, surname, email, date_of_birth, city, phone]
        User_model.edit_user(current_name, data_to_change)

    def get_details_basic(self):
        return [
        self.name,
        self.surname,
        self.email,
        self.date_of_birth,
        self.city,
        self.phone]
