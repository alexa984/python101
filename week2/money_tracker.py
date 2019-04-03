def list_user_data(all_user_data):
    info = ''
    for date, data in all_user_data.items():
        info += '=== {} ===\n'.format(date)
        for inc in data['income']:
            info+='{}, {}, New Income\n'.format(inc[0], inc[1])
        for exp in data['expense']:
            info+='{}, {}, New Expense\n'.format(inc[0], inc[1])

    print(info)


def show_user_incomes(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        income_list = curr_data['income']

        for item in income_list:
            income = (item[0], item[1].strip(), 'New Income')
            result.append(income)

    print(result)


def show_user_savings(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        income_list = curr_data['income']

        for item in income_list:
            income = (item[0], item[1].strip(), 'New Income')
            if item[1] == 'Savings':
                result.append(income)

    print(result)


def show_user_deposits(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        income_list = curr_data['income']

        for item in income_list:
            income = (item[0], item[1].strip(), 'New Income')
            if item[1] == 'Deposit':
                result.append(income)

    print(result)


def show_user_expenses(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        expense_list = curr_data['expense']
        for item in expense_list:
            expense = (item[0], item[1].strip(), 'New Expense')
            result.append(expense)

    print(result)

def list_user_expenses_ordered_by_categories(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        expense_list = curr_data['expense']
        income_list = curr_data['income']
        for item in expense_list:
            expense = (item[0], item[1].strip())
            result.append(expense)

    print(sorted(result, key=lambda x: x[1]))



def show_user_data_per_date(date, all_user_data):
    result = []
    try:
        curr_data = all_user_data[date]
    except:
        KeyError
        print("No items saved for this date.")
    else:
        expense_list = curr_data['expense']
        income_list = curr_data['income']
        for item in expense_list:
            expense = (item[0], item[1], 'New Expense')
            result.append(expense)

        for item in income_list:
            income = (item[0], item[1].strip(), 'New Income')
            result.append(income)

            print(result)


def list_income_categories(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        income_list = curr_data['income']

        for item in income_list:
            result.append(item[1].strip())

    print(result)


def list_expense_categories(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        expense_list = curr_data['expense']
        for item in expense_list:
            expense = (item[0], item[1].strip())
            result.append(expense)

    return sorted(result, key=lambda x: x[1])


def add_income(income_category, money, date, all_user_data):
    to_add = (money, income_category)
    try:
        all_user_data[date]['income'].append(to_add)
    except KeyError:
        all_user_data[date]={'expense': [], 'income':[]}
        all_user_data[date]['income'].append(to_add)
    finally:
        parse_from_dict_to_file(all_user_data)

def add_expense(expense_category, money, date, all_user_data):
    to_add = (money, expense_category)
    try:
        all_user_data[date]['income'].append(to_add)
    except KeyError:
        all_user_data[date]={'expense': [], 'income':[]}
        all_user_data[date]['expense'].append(to_add)
    finally:
        parse_from_dict_to_file(all_user_data)


def parse_from_file_to_dict(filename):
    all_user_data = {}
    try:
        f = open(filename, 'r+')
    except:
                FileNotFoundError
                print("Error loading the information file")
    else:
        for line in f:
            if line[0]==line[1]==line[2]=='=':
                #it is a date line
                date = line.replace('=', '')
                date = date.strip()
                all_user_data[date] = {'expense': [],
                                    'income': []}
            else:
                money, category, type_income_or_expense = line.split(', ')
                type_income_or_expense = type_income_or_expense.strip('\n')
                money = float(money)
                if type_income_or_expense == 'New Income':
                    all_user_data[date]['income'].append((money, category))
                elif type_income_or_expense =='New Expense':
                    (all_user_data[date]['expense']).append((money, category))
    finally:
        f.close()
    
    return all_user_data


def parse_from_dict_to_file(all_user_data):
    info = ''
    for date, data in all_user_data.items():
        info += '=== {} ===\n'.format(date)
        for inc in data['income']:
            info+='{}, {}, New Income\n'.format(inc[0], inc[1])
        for exp in data['expense']:
            info+='{}, {}, New Expense\n'.format(inc[0], inc[1])
    f = open("money_tracker.txt", "w")
    f.write(info)
    f.close()


def print_menu():
    print('Choose one of the following options to continue:')
    print('1 - show all data') #done, working
    print('2 - show data for specific date') 
    print('3 - show expenses, ordered by categories')
    print('4 - add new income')
    print('5 - add new expense')
    print('6 - exit')


def main():
    print_menu()
    command = int(input())
    while command != 6:
        if command < 1 or command > 6:
            print('Invalid command')
        else:
            all_user_data = parse_from_file_to_dict('money_tracker.txt')
            if command == 1:
                list_user_data(all_user_data)
            elif command == 2:
                date = input('Enter date: ')
                show_user_data_per_date(date, all_user_data)
            elif command == 3:
                show_user_expenses_ordered_by_categories(all_user_data)
            elif command == 4:
                category = input('Enter category: ')
                money = float(input('Enter money: '))
                date = input('Enter date: ')
                all_user_data = add_income(category, money, date, all_user_data)
            elif command == 5:
                category = input('Enter category: ')
                money = float(input('Enter money: '))
                date = input('Enter date: ')
                all_user_data = add_income(category, money, date, all_user_data)

        print_menu()
        command = int(input())


if __name__ == '__main__':
    main()
