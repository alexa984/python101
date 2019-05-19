from login_view import LoginView
from register_view import RegisterView
class MainMenuView:
    MAIN_MENU={
        1: 'login',
        2: 'register'
    }
    @classmethod
    def show_options(cls):
        #print menu
        print("""
        1 - Login
        2 - Register
        """)

        #get user input
        try:
            selected = int(input('Select option: '))
            if selected < 1 or selected > 2:
                raise ValueError
            
            #call the needed view
        except ValueError:
            print('Invalid option!')
        

if __name__ == '__main__':
    MainMenuView.show_options()