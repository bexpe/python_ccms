class Employee(User):
    _employee_list = []
    FILE = 'data/employees.csv'

    def __init__(self, name, surname, email, date_of_birth, city, phone, id=None, password=None):
        """
        Initialize Employee object
        :param name:
        :param surname:
        :param email:
        :param date_of_birth:
        :param city:
        :param phone:
        :param id:
        :param password:
        """
        super().__init__(name, surname, email, date_of_birth, city, phone)

        if id is None:
            self.id = User.generate_random(Employee._employee_list)
        else:
            self.id = id

        if password is None:
            hash_object = hashlib.md5(self.username.lower().encode())
            self.password = hash_object.hexdigest()
        else:
            self.password = password

        if self.__class__ == Employee:
            self._employee_list.append(self)

    @classmethod
    def objects_to_list(cls):
        """
        Returns employee list of strings
        :return: employee info: list
        """
        employee_list = []

        for person in cls._employee_list:
            employee_list.append(
                [person.name, person.surname, person.email, person.date_of_birth, person.city, person.phone, person.id,
                 person.password])
        return employee_list

    @classmethod
    def save_employees_csv(cls):
        """
        Saves list of employees objects to csv.
        :return: none
        """
        cls.list_to_csv()

    @classmethod
    def load_employees_csv(cls):
        """
        Loads from csv and creates Employee objects.
        :return: None
        """
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])

    @classmethod
    def get_employees_objects(cls):
        """
        Gives employees objects list

        :return: list of employees objects
        """
        return cls._employee_list

    @classmethod
    def get_employees_objects(cls):
        """
        :return: employee list of objects
        """
        return cls._employee_list