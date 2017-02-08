class Manager(Employee):
    _manager_list = []
    FILE = 'data/managers.csv'

    def __init__(self, name, surname, email, date_of_birth, city, phone, id=None, password=None):
        super().__init__(name, surname, email, date_of_birth, city, phone)

        if id is None:
            self.id = User.generate_random(Manager._manager_list)
        else:
            self.id = id

        if password is None:
            hash_object = hashlib.md5(self.username.lower().encode())
            self.password = hash_object.hexdigest()
        else:
            self.password = password

        self._manager_list.append(self)

    @classmethod
    def objects_to_list(cls):
        """
        Convert objects from objects list to list of lists

        :return: list: list with lists with persons' data
        """

        list_to_write = []

        for person in cls._manager_list:
            list_to_write.append(
                [person.name, person.surname, person.email, person.date_of_birth, person.city, person.phone, person.id,
                 person.password])
        return list_to_write

    @classmethod
    def save_manager_csv(cls):
        """
        Runs list_to_csv for saving list to file
        :return: None
        """
        cls.list_to_csv()

    @classmethod
    def load_manager_csv(cls):
        """
        Read data from file and runs init for every line in file
        :return: None
        """
        with open(cls.FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                Manager(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])

    @classmethod
    def get_managers_objects(cls):
        return cls._manager_list

    @classmethod
    def get_managers_objects(cls):
        """
        :return: list of managers objects
        """
        return cls._manager_list