from user_model import User
class Patient(User):
    def __init__(self, id, username, pass_hash, full_name, age):
        super().__init__(id, username, pass_hash, 'patient')
        self._age = age
        self._full_name = full_name
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    def add_patient(self):
        pass

    def see_patient_by_name(self, name):
        pass

    def see_patient_by_uid(self, uid):
        pass

    