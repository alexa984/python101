from utils.database import Database
class User:
    #eventually make user singleton
    db = Database()
    def __init__(self, uid, username, hashed_password, user_type):
        self._id = uid
        self._username = username
        self._hashed_password = hashed_password
        self._user_type = user_type

    def get_user_type(self):
        return self._user_type
    
    @classmethod
    def create_user(cls, uid, username, hashed_password, user_type):
        cls.db.create_new_user(uid, username, hashed_password, user_type)


