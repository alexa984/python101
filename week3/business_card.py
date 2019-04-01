from sys import argv, stdout
from xml.etree import ElementTree as ET
import json

def business_card():
    my_json_file = argv[1]
    with open(my_json_file, 'r+') as json_file:
        json_data = json.load(json_file)
        all_file_names = []
        for person in json_data['people']:
            full_name = person['first_name'] + ' ' + person['last_name']
            
            html = ET.Element('html')
            head = ET.Element('head')
            html.append(head)
            title = ET.Element('title')
            title.text = full_name
            head.append(title)
            style_link = ET.Element('link', attrib={'rel':'stylesheet', 'type':'text/css', 'href':'styles.css'})
            head.append(style_link)
            body = ET.Element('body')
            html.append(body)
            if person['gender']=='male':
                div_business_card = ET.Element('div', attrib={'class': 'business_card male'})
            elif person['gender']=='female':
                div_business_card = ET.Element('div', attrib={'class': 'business_card female'})
            else:
                 div_business_card = ET.Element('div', attrib={'class': 'business_card'})
            body.append(div_business_card)
            h1_full_name = ET.Element('h1', attrib = {'class':'full-name'})
            h1_full_name.text = full_name
            div_business_card.append(h1_full_name)
            avatar_name = str.format('avatars/{0}', person['avatar'])
            img_avatar = ET.Element('img', attrib = {'class':'avatar', 'src': avatar_name})
            div_business_card.append(img_avatar)
            div_base_info = ET.Element('div', attrib = {'class':'base-info'})
            div_business_card.append(div_base_info)
            p_age = ET.Element('p')
            p_age.text = str.format('Age: {0}', person['age'])
            div_base_info.append(p_age)
            p_birth_date = ET.Element('p')
            p_birth_date.text = str.format('p_birth_date: {0}', person['birth_date'])
            div_base_info.append(p_birth_date)
            p_birth_place = ET.Element('p')
            p_birth_place.text = str.format('Birth_place: {0}', person['birth_place'])
            div_base_info.append(p_birth_place)
            p_gender = ET.Element('p')
            p_gender.text = str.format('Gender: {0}', person['gender'])
            div_base_info.append(p_gender)
            div_interests = ET.Element('div', attrib={'class':'interests'})
            div_business_card.append(div_interests)
            h2_interests = ET.Element('h2')
            h2_interests.text = 'Interests: '
            div_interests.append(h2_interests)
            ul_interests = ET.Element('ul')
            div_interests.append(ul_interests)
            for interest in person['interests']:
                li_int = ET.Element('li')
                li_int.text = interest
                ul_interests.append(li_int)

            div_skills = ET.Element('div', attrib={'class':'skills'})
            div_business_card.append(div_skills)
            h2_skills = ET.Element('h2')
            h2_skills.text = 'Skills: '
            div_skills.append(h2_skills)
            ul_skills = ET.Element('ul')
            div_skills.append(ul_skills)
            for skill in person['skills']:
                li_skill = ET.Element('li')
                name = skill['name']
                level = skill['level']
                li_skill.text = name + ' ' +str(level)
                ul_skills.append(li_skill)

            html_doc_name = str.format('{0}_{1}.html', person['first_name'], person['last_name'])
            ET.ElementTree(html).write(open(html_doc_name, 'w+'), encoding='unicode', method = 'html')
            all_file_names.append(html_doc_name)

        return all_file_names

def main():
    print(business_card())

if __name__ == '__main__':
    # filename = sys.argv[2]
    main()

