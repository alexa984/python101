from sys import argv
import json
def coding_skills():
    my_json_file = argv[1]
    with open(my_json_file, 'r+') as json_file:
        json_data = json.load(json_file)
        all_skills = dict()
        #loads the whole json file in the python dict json_data
        for person in json_data['people']:
            skills = person['skills']
            for skill in skills:
                if all_skills.get(skill['name']) == None or all_skills[skill['name']][0]< skill['level']:
                    all_skills[skill['name']] = [skill['level'], person['first_name'], person['last_name']]

        for skill, info in all_skills.items():
            print(skill + ': ' + info[1] + ' ' + info[2])



coding_skills()
