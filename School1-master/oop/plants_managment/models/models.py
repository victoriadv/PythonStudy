import json
from oop.plants_managment.framework.models import *
class Plant(Model):
    file = "database/plants.json"
    fields = ["name", "address"]

    def __init__(self, name, address, id=None):
        self.name = name
        self.address = address
        self.id = id

    @classmethod
    def get_el_by_id(cls, id):
        data = cls.get_file_data()
        if cls.check_id(id):
            for el in data:
                if el["id"] == id:
                    return cls(el["name"], el["address"], id=el["id"])
        else:
            print("No object with this id\n")


class Salon(Model):
    file = "database/salons.json"
    fields = ["name", "address"]

    def __init__(self, name, address, id=None):
        self.name = name
        self.address = address
        self.id = id

    @classmethod
    def get_el_by_id(cls, id):
        data = cls.get_file_data()
        if cls.check_id(id):
            for el in data:
                if el["id"] == id:
                    return cls(el["name"], el["address"], id=el["id"])
        else:
            print("No object with this id\n")

class Employee(Model):
    file = "database/employees.json"
    fields = ["name", "email", "type_place", "place_id"]

    def __init__(self, name, email, type_place, place_id, id=None):
        self.name = name
        self.email = email
        self.type_place = type_place
        self.place_id = place_id
        self.id = id

    def __getitem__(self, key):
        return self.__dict__[key]

    @classmethod
    def get_el_by_id(cls, id):
        data = cls.get_file_data()
        if cls.check_id(id):
            for el in data:
                if el["id"] == id:
                    return cls(el["name"], el["email"], el["type_place"], el["place_id"], id=el["id"])
        else:
            print("No object with this id\n")


    @classmethod
    def get_info_about_work(cls, id):
        employee = cls.get_el_by_id(id)
        try:
            if employee["type_place"] == "salon":
                salons = Salon.get_file_data()
                for salon in salons:
                    if salon["id"] == employee["place_id"]:
                        print("Salon name: " + salon["name"] + "\nSalon address: " + salon["address"])
            elif employee["type_place"] == "plant":
                plants = Plant.get_file_data()
                for plant in plants:
                    if plant["id"] == employee["place_id"]:
                        print("Plant name: " + plant["name"] + "\nPlant address: " + plant["address"])
            else:
                print("Don`t have this place of work in database")
        except TypeError:
            pass



