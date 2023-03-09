import re

from pprint import pprint

import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

phone_pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_sub = r'+7(\2)-\3-\4-\5 \6\7'

def main(contact_list: list):
    new_list = list()
    for i in contact_list:
        full_name = ' '.join(i[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], i[3], i[4], re.sub(phone_pattern, phone_sub, i[5]), i[6]]
        new_list.append(result)
    return combined(new_list)

def combined(contacts: list):
    for contact in contacts:
        first_name = contact[0]
        last_name = contact[1]
        for app_contact in contacts:
            app_first_name = app_contact[0]
            app_last_name = app_contact[1]
            if first_name == app_first_name and last_name == app_last_name:
                if contact[2] == "": contact[2] = app_contact[2]
                if contact[3] == "": contact[3] = app_contact[3]
                if contact[4] == "": contact[4] = app_contact[4]
                if contact[5] == "": contact[5] = app_contact[5]
                if contact[6] == "": contact[6] = app_contact[6]
        result_list = list()
        for i in contacts:
            if i not in result_list:
                result_list.append(i)

        return result_list


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(main(contacts_list))








