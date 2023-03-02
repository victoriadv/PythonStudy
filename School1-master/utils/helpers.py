import json
import re
import os

def create_file():
    f = open("database/persons.json", "w")
    f.write("[]")
    f.close()

def get_all_humans() -> list:
    try:
        f = open("database/persons.json", "r")
    except FileNotFoundError:
        if os.path.exists("database"):
            create_file()
        else:
            os.mkdir("database")
            create_file()
        f = open("database/persons.json", "r")
    data = json.loads(f.read())
    f.close()
    return data

def check_email(email):
    match = re.search(r'[\w.-]+@[\w.-]+', email)
    if match:
        return True
    else:
        return False

def is_email_unique(email):
    data = get_all_humans()
    for el in data:
        if el["email"] == email:
            return False
    return True

def write_new_human(human: dict):
    data = get_all_humans()

    while not is_email_unique(human["email"]):
        print("Еhis email already exists in the database")
        human["email"] = input("Enter new email: ")

    while not check_email(human["email"]):
        print("Email is not correct")
        human["email"] = input("Enter new email: ")


    if len(data) < 1:
        human["id"] = 1
    else:
        human["id"] = len(data) + 1

    data.append(human)
    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()


def edit_human(id):
    data = get_all_humans()
    for el in data:
        if el["id"] == id:
            el["first_name"] = input("Enter new first name: ")
            el["last_name"] = input("Enter new last name: ")
            el["email"] = input("Enter new email: ")

            while not is_email_unique(el["email"]):
                print("Еhis email already exists in the database")
                el["email"] = input("Enter new email: ")

            while not check_email(el["email"]):
                print("Email is not correct")
                el["email"] = input("Enter new email: ")

    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()





