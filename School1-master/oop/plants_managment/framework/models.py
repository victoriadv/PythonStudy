import json
from abc import ABC, abstractmethod


class Model(ABC):
    file = ""
    fields = []

    # @classmethod
    # def generate_dict(cls):
    #     dictionary = {}
    #     for key in cls.fields:
    #         dictionary[key] = cls.fields[key]
    #     return dictionary

    def generate_dict(self):
        return self.__dict__
    @classmethod
    @abstractmethod
    def get_el_by_id(cls, id):
        pass

    @classmethod
    def get_all(cls):
        data = cls.get_file_data()
        for el in data:
            for key in cls.fields:
                print(el[key])
            print("\n")


    @classmethod
    def get_file_data(cls):
        file = open(cls.file, "r")
        data = json.loads(file.read())
        file.close()
        return data

    @classmethod
    def save_to_file(cls, data):
        file = open(cls.file, "w")
        file.write(json.dumps(data))
        file.close()

    def save(self):
        data = self.get_file_data()
        new_el = self.generate_dict()
        if len(data) >= 1:
            new_el["id"] = len(data) + 1
        else:
            new_el["id"] = 1
        data.append(new_el)
        self.save_to_file(data)

    def update(self):
        data = self.get_file_data()
        for el in data:
            if el["id"] == self.id:
                for key in self.fields:
                    el[key] = input("Type a new " + key + ": ")
        self.save_to_file(data)

    @classmethod
    def check_id(cls, id):
        data = cls.get_file_data()
        for el in data:
            if el["id"] == id:
                return True
        return False
