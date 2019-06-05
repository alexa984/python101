import sqlite3
from sqlite3 import Error
from time import sleep

class Database:
    def __init__(self):
        self.db_path = "/home/alexandra/Documents/python101/hospital/utils/hospital.db"
        #todo: connection to be made once and make it singleton
    
    def create_new_user(self, uid, username, hashed_password, user_type):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            user_info = ( uid, username, hashed_password, user_type, )
            cursor.execute("""
            INSERT INTO User(id, username, hashed_password, user_type)
            VALUES(?, ?, ?, ?);
            """, user_info)
            connection.commit()
        except sqlite3.Error as e:
            print('Some error occured while creating your profile. We are sorry. Try again.', e)
            sleep(3)
            connection.rollback()
            exit(1)
        finally:
            connection.close()

    def create_new_doctor(self, uid, full_name, specialty, phone_number):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            doctor_info = ( uid, full_name, specialty, phone_number, )
            cursor.execute("""
            INSERT INTO Doctor(user_id, full_name, specialty, phone)
            VALUES(?, ?, ?, ?);
            """, doctor_info)
            connection.commit()
        except sqlite3.Error:
            print('Some error occured while creating your doctor profile. We are sorry. Try again.')
            sleep(3)
            exit(2)
        finally:
            connection.close()


    def create_new_patient(self, user_id, full_name, age ):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            patient_info = ( user_id, full_name, age, )
            cursor.execute("""
            INSERT INTO Patient(user_id, full_name, age)
            VALUES(?, ?, ?);
            """, patient_info)
            connection.commit()
        except sqlite3.Error as e:
            print('Some error occured while creating your patient profile. We are sorry. Try again.', e)
            sleep(3)
            exit(3)
        finally:
            connection.close()

    def get_all_patients(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                SELECT full_name
                FROM Patient
                """
            )
            patients = cursor.fetchall()
            connection.commit()
        except sqlite3.Error:
            print("Can't get patients info right now.")
            sleep(3)
            exit(4)
        finally:
            connection.close()
            return patients

    def get_all_doctors(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                    SELECT * 
                    FROM Doctor
                """
            )
            doctors = cursor.fetchall()
            connection.commit()
            return doctors
        except sqlite3.Error:
            print("can't get info about doctors")
            return -1


    def get_user_type_based_on_username(self, username):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                SELECT user_type
                FROM User
                WHERE username = (?)
                """, (username, )
            )
            user_type = cursor.fetchone()
            connection.commit()
        except Exception:
            print("Can't get the type of this user")
            sleep(3)
            exit(5)
        finally:
            connection.close()
            return user_type

    def check_does_user_exist(self, username):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                SELECT username
                FROM User
                WHERE username = (?)
                """, (username, )
            )
            this_username = cursor.fetchone()
            connection.commit()
            if this_username:
                return True
        except sqlite3.Error:
            exit(7)
        finally:
            connection.close()
            return False
    
    def check_username_password_match(self, username, hashed_pass):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                SELECT hashed_password
                FROM User
                WHERE username = (?)
                """, (username, )
            )
            this_user_password = cursor.fetchone()
            connection.commit()
            if this_user_password[0]==hashed_pass:
                return True
            else:
                return False
        except TypeError:
            print("This user doesn't exist")
        except Exception as e:
            print('Invalid login', e)
            sleep(3)
        finally:
            connection.close()


    def show_all_patients(self, doctor_uid):
        pass

    def return_login_info_patient(self, username):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                SELECT user_id, full_name, age
                FROM Patient JOIN User ON Patient.user_id=User.id
                WHERE username = (?)
                """, (username, )
            )
            this_user_id, this_user_name, this_user_age = cursor.fetchmany()
            connection.commit()
            return this_user_id, this_user_name, this_user_age
        except Exception:
            print('Invalid login')
            sleep(3)
        finally:
            connection.close()

    def return_login_info_doctor(self, username):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                SELECT user_id, full_name, specialty, phone
                FROM Doctor
                WHERE username = (?)
                """, (username, )
            )
            this_user_id, this_user_name, this_user_specialty, this_user_phone = cursor.fetchmany()
            connection.commit()
            return this_user_id, this_user_name, this_user_specialty, this_user_phone
        except Exception:
            print('Invalid login')
            sleep(3)
        finally:
            connection.close()