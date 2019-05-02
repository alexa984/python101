#module should process the user data, This class takes just one attribute - AggregatedMoneyTracker object
from parse_money_tracker_data import parse_from_file_to_dict
from aggregated_money_tracker import aggregate_object
import category

dict_from_data = parse_from_file_to_dict('money_tracker.txt')
data_obj = aggregate_object(dict_from_data)

#define all methods based on data_obj
def list_all_user_data():
    for obj in data_obj:
        print(obj.amount, obj.for_what, obj._type, obj.date)

def show_user_incomes():
    for obj in data_obj:
        if isinstance(obj, Income):
            print(obj.amount, obj.for_what, obj._type, obj.date)

def show_user_expenses():
    for obj in data_obj:
        if isinstance(obj, Expense):
            print(obj.amount, obj.for_what, obj._type, obj.date)

def show_user_data_per_date(date):
    for obj in data_obj:
        if obj.date == date:
            print(obj.amount, obj.for_what, obj._type, obj.date)

def add_income(categ, money, date):
    data_obj.append(category.Income(money, categ, date))

def add_expense(categ, money, date):
    data_obj.append(category.Expense(money, categ, date))