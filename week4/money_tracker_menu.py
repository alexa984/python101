#money_tracker_menu.py is responsible to call the MoneyTracker methods based on the option provided from the user
import money_tracker
def print_menu():
    print('Choose one of the following options to continue:')
    print('1 - show all data') #done, working
    print('2 - show data for specific date') 
    print('3 - show expenses, ordered by categories')
    print('4 - add new income')
    print('5 - add new expense')
    print('6 - exit')

def operate_menu():
    print_menu()
    command = int(input())
    while command != 6:
        if command < 1 or command > 6:
            print('Invalid command')
        else:
            if command == 1:
                money_tracker.list_all_user_data()
            elif command == 2:
                date = input('Enter date: ')
                money_tracker.show_user_data_per_date(date)
            elif command == 3:
                money_tracker.show_user_expenses_ordered_by_categories()
            elif command == 4:
                category = input('Enter category: ')
                money = float(input('Enter money: '))
                date = input('Enter date: ')
                money_tracker.add_income(category, money, date)
            elif command == 5:
                category = input('Enter category: ')
                money = float(input('Enter money: '))
                date = input('Enter date: ')
                money_tracker.add_expense(category, money, date)


        print_menu()
        command = int(input())
