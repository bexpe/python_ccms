import random
import csv
import hashlib


class User:

    def __init__(self, name, surname, email, date_of_birth, city, phone, password=None):
        # if not name or not surname or not email:
        #     raise ValueError("Name, surname and email can't be empty")

        self.name = name
        self.surname = surname
        self.username = self.name[:2] + self.surname[:3]
        # if '@' not in email:
        #     raise NameError("Invalid email")
        self.email = email
        if password is None:
            self.password = self.username.lower()
        else:
            self.password = password
        self.phone = phone
        self.city = city
        self.date_of_birth = date_of_birth

    def get_email(self):
        """
        This method gets an users email
        :return: users email as an object
        """
        return self.email

    def get_password(self):
        """
        This method gets an users password.
        :return: users password as an object
        """
        return self.password

    def change_password(self, new_password):
        """
        Changes an old password

        :param new_password:

        :return: new_password
        """
        self.password = new_password

    @classmethod
    def get_students_objects(cls):
        """
        :return: list of students as a list of objects
        """
        return cls._students_list

    @classmethod
    def list_to_csv(cls):
        """
        Write lists with objects' data to file
        :return: None
        """
        table = cls.objects_to_list()
        with open(cls.FILE, 'w') as file:
            for record in table:
                row = ','.join(record)
                file.write(row + "\n")

    @staticmethod
    def generate_random(table):
        """
        Generates random and unique string. Used for id/key generation.

        Args:
            table: list containing keys. Generated string should be different then all of them

        Returns:
            Random and unique string
        """

        list_of_id = []
        for record in table:
            list_of_id.append(record.id)

        generated = ''

        special_char_index = list(range(33, 48)) + list(range(58, 59)) + list(range(60, 65)) \
            + list(range(91, 97)) + list(range(124, 127))
        start = True
        max_len_id = 3
        while start:
            list_of_char = []
            new_id = ''

            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(str(chr(random.choice(special_char_index))))
            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(str(random.randint(0, 9)))
            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(chr(random.randint(97, 122)).upper())
            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(chr(random.randint(97, 122)))

            for i in range(len(list_of_char)):
                char = random.choice(list_of_char)
                new_id += char
                list_of_char.remove(char)
            if new_id not in list_of_id:
                generated += new_id
                start = False

        return generated

    def edit_user(self):
        """
        Edit student object.
        :return: none
        """
        option = input('Choose what would you like to edit: \n1. name \n, 2. surname \n, 3. date_of_birth \n,'
                       ' 4. city \n, 5. phone \n, 6. all ')
        if option == '1':
            new_name = input('Please type new name: ')
            self.name = new_name
        if option == '2':
            new_surname = input('Please type new surname: ')
            self.surname = new_surname
        if option == '3':
            new_date_of_birth = input('Please type new date of birth: ')
            self.date_of_birth = new_date_of_birth
        if option == '4':
            new_city = input('Please type new city: ')
            self.city = new_city
        if option == '5':
            new_phone = input('Please type new phone: ')
            self.phone = new_phone
        if option == '6':
            new_name = input('Please type new name: ')
            new_surname = input('Please type new surname: ')
            new_date_of_birth = input('Please type new date of birth: ')
            new_city = input('Please type new city: ')
            new_phone = input('Please type new phone: ')
            self.name = new_name
            self.surname = new_surname
            self.date_of_birth = new_date_of_birth
            self.city = new_city
            self.phone = new_phone

    @staticmethod
    def show_list(to_print_list):
        """
        Returns a list as a string with users depending on the class we choose

        :param to_print_list:

        :return: string
        """
        # transposition of list to print, for easy access to columns
        transposed_to_print_list = [list(x) for x in zip(*to_print_list)]

        # evaluate lengths of strings in columns for getting longest strings, to determine columns widths
        columns_widths = []
        for line in transposed_to_print_list:
            max_width = 0
            for item in line:
                if len(str(item)) > max_width:
                    max_width = len(str(item)) + 2
            columns_widths.append(max_width)

        table_str = ""  # string with content of table
        # generate strings for top and bottom of table, and row separator
        pauses = "-" * (sum(columns_widths) + len(to_print_list[0]) - 1)  # create of string with '-' for printing (---)
        top = "/{}\\\n".format(pauses)  # top row of table /----\
        bot = "\\{}/\n".format(pauses)  # bottom row       \----/

        # generate separator row |---|----------|-----| ....
        separator = "|"

        for item in columns_widths:
            separator += '{:^{}}|'.format("-" * (columns_widths[columns_widths.index(item)]),
                                          columns_widths[columns_widths.index(item)] - 1)

        for line in to_print_list:
            i = 0
            table_str += '|'
            for item in line:  # print every item from list from table in format: | column | column | col | ...
                table_str += '{:^{}}|'.format(item, columns_widths[i])
                i += 1

            if line != to_print_list[-1]:  # adds separator after row, except last row (bottom row is adding later)
                table_str += "\n{}\n".format(separator)

        return "{}{}\n{}".format(top, table_str, bot)
