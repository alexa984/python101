def list_user_data(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        expense_list = curr_data['expense']
        income_list = curr_data['income']
        for item in expense_list:
            expense = (item[0], item[1], 'New Expense')
            result.append(expense)

        for item in income_list:
            income = (item[0], item[1].strip(), 'New Income')
            result.append(income)

    return result


def show_user_incomes(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        income_list = curr_data['income']

        for item in income_list:
            income = (item[0], item[1].strip(), 'New Income')
            result.append(income)

    return result


def show_user_savings(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        income_list = curr_data['income']

        for item in income_list:
            income = (item[0], item[1].strip(), 'New Income')
            if item[1] == 'Savings':
                result.append(income)

    return result


def show_user_deposits(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        income_list = curr_data['income']

        for item in income_list:
            income = (item[0], item[1].strip(), 'New Income')
            if item[1] == 'Deposit':
                result.append(income)

    return result


def show_user_expenses(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        expense_list = curr_data['expense']
        for item in expense_list:
            expense = (item[0], item[1].strip(), 'New Expense')
            result.append(expense)

    return result

def list_user_expenses_ordered_by_categories(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        expense_list = curr_data['expense']
        income_list = curr_data['income']
        for item in expense_list:
            expense = (item[0], item[1].strip())
            result.append(expense)

    return sorted(result, key=lambda x: x[1])



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

    return result


def list_income_categories(all_user_data):
    result = []
    for date in all_user_data:
        curr_data = all_user_data[date]
        income_list = curr_data['income']

        for item in income_list:
            result.append(item[1].strip())

    return result


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
    pass


def add_expense(expense_category, money, date, all_user_data):
    pass


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
    pass


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
            # print(all_user_data.items())
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
                add_income(category, money, date, all_user_data)

        print_menu()
        command = int(input())


if __name__ == '__main__':
    main()
