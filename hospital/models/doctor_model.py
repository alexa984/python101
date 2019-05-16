from user_model import User
class Doctor(User):
    def __init__(self, id, username, pass_hash, full_name, specialty, phone_number):
        super().__init__(id, username, pass_hash, 'doctor')
        self._full_name = full_name
        self._specialty = specialty
        self._phone_number = phone_number

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    @property
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, value):
        self._specialty = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def show_patients(self):
        pass

    def show_examinations_for_day(self):
        pass  

    def show_available_slots(self, date):
        pass

    def search_user_by_id(self, uid):
        pass

    def search_user_by_name(self, name):
        pass