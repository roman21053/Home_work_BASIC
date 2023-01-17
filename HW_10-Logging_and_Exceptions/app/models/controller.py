import logging
from .classes import Plant, Employee


class Controller(Plant, Employee):
    @classmethod
    def check_input_date(cls, data):
        try:
            if len(data) == 0:
                return int(data)
        except ValueError as err:
            logging.error(err)
            raise ValueError('Data not entered. Try again')

    @classmethod
    def check_input_id(cls, id_instance):
        try:
            return int(id_instance)
        except ValueError as err:
            logging.error(err)
            print('entered "id" is not digit.. Try again')

    @classmethod
    def add_new_plant(cls):
        name = input("Type name of new plant: ")
        cls.check_input_date(name)
        location = input("Type location of plant: ")
        cls.check_input_date(location)
        plant = Plant(name, location)
        plant.save()

    @classmethod
    def add_new_employee(cls):
        name = input("Type name of employee: ")
        cls.check_input_date(name)
        email = input("Type email of employee: ")
        cls.check_input_date(email)
        plant_id = cls.check_input_id(input("Type id of plant: "))
        employee = Employee(name, email, plant_id)
        employee.save()

    @classmethod
    def get_all_plants(cls):
        plants = Plant.get_all()
        for plant in plants:
            print("id =", plant["id"], plant["name"], ":", plant["location"])

    @classmethod
    def get_all_employee(cls):
        employees = Employee.get_all()
        for employee in employees:
            print("id employee = ", employee["id"], "; ", employee["name"], ": ", employee["email"], ";  plant id: ",
                  employee["plant_id"], sep=""
                  )

    @classmethod
    def get_plant_by_id(cls):
        id_plant = input("Type id of plant: ")
        cls.check_input_id(id_plant)
        plant = Plant.get_by_id(int(id_plant))
        print("id plant =", plant["id"], plant["name"], ":", plant["location"])

    @classmethod
    def get_employee_by_id(cls):
        id_employee = input("Type id of plant: ")
        cls.check_input_id(id_employee)
        employee = Employee.get_by_id(int(id_employee))
        print("id employee =", employee["id"], employee["name"], ":", employee["email"])

    @classmethod
    def delete_plant_by_id(cls):
        id_plant = input('Type id of plant which you want to delete: ')
        cls.check_input_id(id_plant)
        Plant.delete(int(id_plant))

    @classmethod
    def delete_employee_by_id(cls):
        id_employee = input('Type id of employee which you want to delete: ')
        cls.check_input_id(id_employee)
        Employee.delete(int(id_employee))
