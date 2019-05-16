from hashlib import sha256
class User:
    def __init__(self, id, username, pass_hash, user_type):
        self._id = id
        self._username = username
        self._pass_hash = pass_hash
        self._user_type = user_type

    def get_user_type(self):
        return self._user_type

    def get_pass_hash(self):
        return self._pass_hash

    @staticmethod
    def hash(inpt):
        m = sha256()
        m.update(inpt.encode('utf-8'))
        return m.hexdigest()

