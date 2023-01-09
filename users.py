class User:
    """
    The class is used to keep data about users
    """

    users: dict = {}

    def __init__(self, user_id: int):
        """
        The instance has info about locations (types, what API supports) and user_id from telegram.
        """

        self.user_id = user_id
        User.add_user(user_id=user_id, user=self)

        self.location: str = ''         # name of city
        self.position: dict = {}        # latitude and longitude
        self.woid: str = ''             # id of geographic places used by Yahoo

    @classmethod
    def add_user(cls, user_id: int, user):
        """
        Method to create users, adding to dict.
        """
        cls.users[user_id] = user

    @classmethod
    def get_user(cls, user_id: int):
        """
        Method to get users from dict, if there is no exact instance - adds new user.
        """

        if user_id in cls.users:
            return cls.users.get(user_id)

        User(user_id=user_id)
        return cls.users[user_id]

