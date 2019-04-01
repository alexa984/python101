import csv
def filter(file_name, **kwargs):
  with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    col_names = ['full_name', 'favourite_color', 'company_name', 'email', 'phone_number', 'salary']
    
    for row in csv_reader:
        if line_count > 0:
          
              line_count += 1
        # else:
        #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        #     line_count += 1
    # print(f'Processed {line_count} lines.')
    print(col_names)
filter('example_data.csv', full_name = 'Marissa Carter')