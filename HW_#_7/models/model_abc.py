import json
from abc import ABC


class Model(ABC):
    file = "default.json"

    def save(self):
        file = open("database/" + self.file, "r")
        data_in_json = file.read()
        file.close()
        data = json.loads(data_in_json)
        new_instance = self.__dict__
        if len(data) > 0:
            new_instance["id"] = data[-1]["id"] + 1
        else:
            new_instance["id"] = 1
        data.append(new_instance)
        file = open("database/" + self.file, "w")
        file.write(json.dumps(data))
        file.close()

    @classmethod
    def get_all(cls):
        file = open("database/" + cls.file, "r")
        instances = json.loads(file.read())
        file.close()
        for instance in instances:
            return instance

    @classmethod
    def get_by_id(cls, id):
        file = open("database/" + cls.file, "r")
        instances = json.loads(file.read())
        file.close()
        for instance in instances:
            if instance["id"] == id:
                return instance
