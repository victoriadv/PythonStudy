import json
import re

class Plant:

    file = "database/plants.json"

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def generate_dict(self):
        return {
            "name": self.name,
            "address": self.address
        }

    def save(self):
        file = open(self.file, "r")
        all_obj = json.loads(file.read())
        file.close()
        file = open(self.file, "w")
        new_obj = self.generate_dict()
        if len(all_obj) >= 1:
            new_obj["id"] = len(all_obj) + 1
        else:
            new_obj["id"] = 1
        all_obj.append(new_obj)
        file.write(json.dumps(all_obj))
        file.close()

    @classmethod
    def edit_plant(cls, id):
        plants = cls.get_all()
        for plant in plants:
            if plant["id"] == id:
                plant["name"] = input("Enter new name: ")
                plant["address"] = input("Enter new address: ")
        file = open(cls.file, "w")
        edit_data = json.dumps(plants)
        file.write(edit_data)
        file.close()

    @classmethod
    def get_all(cls):
        file = open(cls.file, "r")
        data = json.loads(file.read())
        file.close()
        return data

class Employee(Plant):

    file = "database/employees.json"

    def __init__(self, name, email, plant_id):
        self.name = name
        self.email = email
        self.plant_id = plant_id


    def generate_dict(self):
        match = re.search(r'[\w.-]+@[\w.-]+', self.email)
        while not match:
            print("Email is not correct")
            self.email = input("Enter new email: ")
            match = re.search(r'[\w.-]+@[\w.-]+', self.email)
        return {
            "name": self.name,
            "email": self.email,
            "plant_id": self.plant_id
        }

    @classmethod
    def edit_employee(cls, id):
        employees = cls.get_all()
        for employee in employees:
            if employee["id"] == id:
                employee["name"] = input("Enter new name: ")
                employee["email"] = input("Enter new email: ")
                employee["plant_id"] = input("Enter new plant_id: ")

        file = open(cls.file, "w")
        edit_data = json.dumps(employees)
        file.write(edit_data)
        file.close()