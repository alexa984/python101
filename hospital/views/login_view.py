from sys import path, exit
from getpass import getpass
path.append('../')
from controllers.controller import MainController
import traceback

class LoginView:
    @classmethod
    def show_login(cls):
        #get user input
        try:
            user_name = input('Username: ')
            password = getpass()
            remaining_try = 3
            status = MainController.login(user_name, password)
            #if username and password doesn't match
            if status == -1:
                remaining_try-=1
                if remaining_try > 0:
                    cls.show_login()
                else:
                    exit()

        except Exception as e:
            print('Login unsuccessful', e)
            tb = traceback.format_exc()
            print(e, tb)
        