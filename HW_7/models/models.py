from model_abc import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employee.json"

    def __init__(self, name, email, plant_id):
        self.name = name
        self.email = email
        self.plant_id = plant_id


class Salon(Model):
    file = "salon.json"

    def __init__(self, name, location, plant_id):
        self.name = name
        self.location = location
        self.plant_id = plant_id
