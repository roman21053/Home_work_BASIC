import logging
from .class_abc import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employee.json"

    def __init__(self, name: str, email: str, plant_id: int):
        self.name = self.check_name(name)
        self.email = email
        self.plant_id = plant_id

    def check_name(self, name):
        for char in name:
            if not char.isdigit():
                continue
            else:
                logging.error('The entered name contains numbers.: ' + str(name))
                raise ValueError('The entered name contains numbers. Try again')
        return name

    def check_email(self):
        data = self.get_all()
        for el in data:
            if self.email == el["email"]:
                raise ValueError("This email already exist!")

    def check_email_format(self):
        if not "@" in self.email or not "." in self.email:
            raise ValueError("Not a valid email address!")
        position = self.email.find("@")
        position_of_dot = self.email.find(".")
        if position > position_of_dot:
            raise ValueError("Not a valid email address!")

    def save(self):
        plant = Plant.get_by_id(self.plant_id)
        try:
            self.check_email()
            self.check_email_format()
        except ValueError as e:
            logging.error(str(e) + " Email: " + self.email)
            print(e)
            return
        if not plant:
            logging.error('id plant does not exist: ' + str(self.plant_id))
            raise ValueError("Plant not found!")
        super().save()
