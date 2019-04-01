#in aggregated_money_tracker.py you need to process the list of rows and create an aggregated object
import category

def aggregate_object(dict_with_records):
    aggregated_categories = []
    for date, info in dict_with_records.items():
        for expense in info['expense']:
            aggregated_categories.append(category.Expense(expense[0], expense[1], date))
        for income in info['income']:
            aggregated_categories.append(category.Income(income[0], expense[1], date))
    return aggregated_categories




