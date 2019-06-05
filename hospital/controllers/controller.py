import binascii
import sys
sys.path.append('../')
from hashlib import sha256
from utils.database import Database
from models.user_model import User
from models.doctor_model import Doctor
from models.patient_model import Patient

class MainController:
    db = Database()
    curr_user = None
    @classmethod
    def login(cls, username, password):
        hashed_password = cls.hash_pass(password)
        if cls.db.check_username_password_match(username, hashed_password):
            user_type = cls.db.get_user_type_based_on_username(username)
            if user_type == 'patient':
                Patient.login(username, hashed_password)
            elif user_type == 'doctor':
                Doctor.login(username, hashed_password)
            return 1
        else:
            print('Invalid username or password')
            return -1
        
            
    @classmethod
    def register(cls, **kwargs):
        
        if cls.db.check_does_user_exist(kwargs['username']):
            print('this user already exists')
        else:
            if kwargs['user_type'] == 'doctor':
                #create doctor
                hashed_password = cls.hash_pass(kwargs['password'])
                cls.curr_user = Doctor.create_doctor(kwargs['uid'], kwargs['username'], hashed_password, kwargs['full_name'], kwargs['specialty'], kwargs['phone_number'])
                
            elif kwargs['user_type'] == 'patient':
                #create patient
                hashed_password = cls.hash_pass(kwargs['password'])
                cls.curr_user = Patient.add_patient(kwargs['uid'], kwargs['username'], hashed_password, kwargs['full_name'], kwargs['age'])
            else:
                print('Invalid user type')

    @classmethod
    def show_all_doctors(cls):
        doctors = cls.db.get_all_doctors()
        for doctor in doctors:
            print (doctor)

    @staticmethod
    def hash_pass(inpt):
        return sha256(str(inpt).encode('utf-8')).hexdigest()


    # @staticmethod
    # def hash(string):
    #     bina = binascii.unhexlify(string)
    #     hash = sha256(sha256(bina).digest()).digest()
    #     raw = str(binascii.hexlify(hash))[2:-1]
    #     return raw

