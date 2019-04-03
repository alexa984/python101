import csv
def filter_csv(file_name, **kwargs):
    filter_kwargs = ['full_name', 'favourite_color', 'company_name', 'email', 'phone_number', 'salary']

    with open(file_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for pos, kw in enumerate(filter_kwargs):
            if kw in kwargs:
                csvreader = list(filter(lambda p: kwargs[kw] == p[pos], csvreader))

        return csvreader


# filter_csv("example_data.csv", full_name="Diana Harris", favourite_color='lime' )