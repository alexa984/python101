# from hashlib import sha256
from utils.database import Database
class User:
    db = Database()
    def __init__(self, id, username, hashed_password, user_type):
        self._id = id
        self._username = username
        self._hashed_password = hashed_password
        self._user_type = user_type

    def get_user_type(self):
        return self._user_type

    @classmethod
    def login(cls, username, hashed_password):
        if cls.db.get_user_type_based_on_username(username) == 'patient':
            #call the login for patient
            pass
        elif cls.db.get_user_type_based_on_username(username) == 'doctor':
            #call the login for patient
            pass
    
    @classmethod
    def create_user(cls, id, username, hashed_password, user_type):
        cls.db.create_new_user(id, username, hashed_password, user_type)
        return cls(id, username, hashed_password, user_type)

