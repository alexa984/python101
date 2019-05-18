from hashlib import sha256
from models import user_model
from utils.database import Database
from models.user_model import User
from models.doctor_model import Doctor
from models.patient_model import Patient
class MainController:
    db - Database()

    @classmethod
    def login(cls, username, password):
        password = hash(password)
        if cls.db.check_username_password_match(username, password):
            curr_user = user_model.User.login(username, password)
        else:
            print('Invalid username or password')

    @classmethod
    def register(cls, **kwargs):
        if cls.db.check_does_user_exist(kwargs['username']):
            print('this user already exists')
        else:
            if kwargs['user_type'] == 'doctor':
                #create doctor
                hashed_password = hash(kwargs['password'])
                curr_user = Doctor.create_doctor(kwargs['uid'], kwargs['username'], hashed_password, kwargs['full_name'], kwargs['specialty'], kwargs['phone_number'])
                
            elif kwargs['user_type'] == 'patient':
                #create patient
                hashed_password = hash(kwargs['password'])
                curr_user = Patient.add_patient(kwargs['uid'], kwargs['username'], hashed_password, kwargs['phone_number'], kwargs['age'])
            else:
                print('Invalid user type')



    @staticmethod
    def hash(inpt):
        m = sha256()
        m.update(inpt.encode('utf-8'))
        return m.hexdigest()

