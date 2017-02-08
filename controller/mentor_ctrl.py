class Mentor(Employee):
    _mentor_list = []
    FILE = 'data/mentors.csv'

    def __init__(self, name, surname, email, date_of_birth, city, phone, id=None, password=None):
        super().__init__(name, surname, email, date_of_birth, city, phone)

        if id is None:
            self.id = User.generate_random(Mentor._mentor_list)
        else:
            self.id = id

        if password is None:
            hash_object = hashlib.md5(self.username.lower().encode())
            self.password = hash_object.hexdigest()
        else:
            self.password = password

        self._mentor_list.append(self)

    @classmethod
    def objects_to_list(cls):
        """
        Convert objects from objects list to list of lists

        :return: list: list with lists with persons' data
        """

        list_to_write = []

        for person in cls._mentor_list:
            list_to_write.append(
                [person.name, person.surname, person.email, person.date_of_birth, person.city, person.phone, person.id,
                 person.password])
        return list_to_write

    @classmethod
    def mentor_list_basics(cls):
        mentor_basics_list = []
        for mentor in cls._mentor_list:
            mentor_basics_list.append('\n name: {} surname: {} email: {}'.format(
                mentor.name, mentor.surname, mentor.email))
        return "".join(mentor_basics_list)

    @classmethod
    def get_mentor_from_list_by_id(cls, mentor_id):
        for mentor in cls._mentor_list:
            if mentor.id == mentor_id:
                return mentor

    @classmethod
    def remove_mentor_from_list(cls, mentor_id):
        for mentor in cls._mentor_list:
            if mentor.id == mentor_id:
                cls._mentor_list.remove(mentor)

    @classmethod
    def load_mentor_csv(cls):
        """
        Read data from file and runs init for every line in file
        :return: None
        """
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Mentor(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])

    @classmethod
    def save_mentor_csv(cls):
        """
        Runs list_to_csv for saving list to file
        :return: None
        """
        cls.list_to_csv()

    def edit_mentor(cls):
        option = input('Choose what would you like to edit: 1. name \n, 2. surname \n, 3. date_of_birth \n, 4. city \n,'
                       ' 5. phone \n, 6. all')
        if option == '1':
            new_name = input('Please type new name: ')
            cls.name = new_name
        if option == '2':
            new_surname = input('Please type new surname: ')
            cls.surname = new_surname
        if option == '3':
            new_date_of_birth = input('Please type new date of birth: ')
            cls.date_of_birth = new_date_of_birth
        if option == '4':
            new_city = input('Please type new city: ')
            cls.city = new_city
        if option == '5':
            new_phone = input('Please type new phone: ')
            cls.phone = new_phone
        if option == '6':
            new_name = input('Please type new name: ')
            new_surname = input('Please type new surname: ')
            new_date_of_birth = input('Please type new date of birth: ')
            new_city = input('Please type new city: ')
            new_phone = input('Please type new phone: ')
            cls.name = new_name
            cls.surname = new_surname
            cls.date_of_birth = new_date_of_birth
            cls.city = new_city
            cls.phone = new_phone

    @classmethod
    def get_mentor_list(cls):
        """Returns string with table to print"""
        list_to_print = cls.get_list_to_print()
        table = cls.show_list(list_to_print)
        return table

    @classmethod
    def get_list_to_print(cls):
        """Returns list with list made from objects data"""
        header_row = ['Name', 'Surname', 'email', 'Date_of_birth', 'Phone number']
        to_print_list = [header_row]
        for mentor in cls._mentor_list:
            to_print_list.append(
                [mentor.name, mentor.surname, mentor.email, mentor.date_of_birth, mentor.phone])
        return to_print_list

    @classmethod
    def get_mentors_objects(cls):
        return cls._mentor_list