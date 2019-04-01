#in parse_money_tracker_data.py you have to parse the data 
#coming from money_tracker.txt and return list of the rows

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
