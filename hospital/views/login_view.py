from sys import path, exit
path.append('../')
from controllers.controller import MainController
class LoginView:
    @staticmethod
    def show_login():
        #get user input
        try:
            user_name = input('Enter username: ')
            password = input('Enter password: ')
            remaining_try = 3
            status = MainController.login(user_name, password)
            #if username ad password doesn't match
            if status == -1:
                remaining_try-=1
                if remaining_try > 0:
                    show_login()
                else:
                    exit()

        except:
            print('Login unsuccessful')
        