import sqlite3
from sqlite3 import Error
from time import sleep
from sys import exit
class Database:
    def __init__(self):
        self.db_path = "/home/alexandra/Documents/python101/hospital/utils/hospital.db"

    def create_new_user(self, uid, username, hashed_password, user_type):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            user_info = ( uid, username, hashed_password, user_type )
            cursor.executemany("""
            INSERT INTO User(id, username, hashed_password, user_type)
            VALUES(?, ?, ?, ?);
            """, user_info)
            connection.commit()
        except Exception:
            print('Some error occured while creating your profile. We are sorry. Try again.')
            sleep(3)
            exit(1)
        finally:
            connection.close()

    def create_new_doctor(self, uid, full_name, specialty, phone_number):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            doctor_info = ( uid, full_name, specialty, phone_number )
            cursor.executemany("""
            INSERT INTO Doctor(user_id, full_name, specialty, phone)
            VALUES(?, ?, ?, ?);
            """, doctor_info)
            connection.commit()
        except Exception:
            print('Some error occured while creating your profile. We are sorry. Try again.')
            sleep(3)
            exit(2)
        finally:
            connection.close()


    def create_new_patient(self, user_id, full_name, age ):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            patient_info = ( user_id, full_name, age )
            cursor.executemany("""
            INSERT INTO Doctor(user_id, full_name, age)
            VALUES(?, ?, ?);
            """, patient_info)
            connection.commit()
        except Exception:
            print('Some error occured while creating your profile. We are sorry. Try again.')
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
        except Exception:
            print("Can't get patients info right now.")
            sleep(3)
            exit(4)
        finally:
            connection.close()
            return patients


    def get_user_type_based_on_id(self, uid):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                SELECT user_type
                FROM User
                WHERE id = ?
                """, uid
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

