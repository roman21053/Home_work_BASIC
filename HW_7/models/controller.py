from models import Plant, Employee, Salon


class Controller(Plant, Employee, Salon):

    @classmethod
    def add_new_plant(cls):
        name = input("Type name of new plant: ")
        location = input("Type location of plant: ")
        plant = Plant(name, location)
        plant.save()

    @classmethod
    def add_new_employee(cls):
        name = input("Type name of employee: ")
        email = input("Type email of employee: ")
        plant_id = int(input("Type id of plant: "))
        employee = Employee(name, email, plant_id)
        employee.save()

    @classmethod
    def add_new_salon(cls):
        name = input("Type name of salon: ")
        location = input("Type location of salon: ")
        plant_id = int(input("Type id of plant: "))
        salons = Salon(name, location, plant_id)
        salons.save()

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
    def get_all_salons(cls):
        salons = Salon.get_all()
        for salon in salons:
            print("id salon =", salon["id"], "; ", salon["name"], ":", salon["location"], "; ",  "plant id: ",
                  salon["plant_id"], sep=""
                  )

    @classmethod
    def get_plant_by_id(cls):
        id = int(input("Type id of plant: "))
        plant = Plant.get_by_id(id)
        print("id plant =", plant["id"], plant["name"], ":", plant["location"])

    @classmethod
    def get_employee_by_id(cls):
        id = int(input("Type id of plant: "))
        employee = Employee.get_by_id(id)
        print("id employee =", employee["id"], employee["name"], ":", employee["email"])

    @classmethod
    def get_salon_by_id(cls):
        id = int(input("Type id of plant: "))
        salon = Salon.get_by_id(id)
        print("id salon =", salon["id"], salon["name"], ":", salon["location"])

    @classmethod
    def delete_plant_by_id(cls):
        id = int(input('Type id of plant which you want to delete: '))
        Plant.delete(id)

    @classmethod
    def delete_employee_by_id(cls):
        id = int(input('Type id of employee which you want to delete: '))
        Employee.delete(id)

    @classmethod
    def delete_salon_by_id(cls):
        id = int(input('Type id of salon which you want to delete: '))
        Salon.delete(id)
