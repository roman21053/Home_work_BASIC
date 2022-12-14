from models.models import Plant, Employee

while True:
    print(
        "\n1. Add new plant \n"
        "2. Get all plants\n"
        "3. Get plant by id\n"
        "4. Delete plant by id\n"
        "5. Add new employee\n"
        "6. Get all employee\n"
        "7. Get employee by id\n"
        "8. Delete employee by id\n"
    )
    flag = int(input("Choose: "))
    if flag == 1:
        name = input("Type name of new plant: ")
        location = input("Type location of plant: ")
        plant = Plant(name, location)
        plant.save()
    if flag == 2:
        plants = Plant.get_all()
        for plant in plants:
            print("id =", plant["id"], plant["name"], ":", plant["location"])
    if flag == 3:
        id = int(input("Type id of plant: "))
        plant = Plant.get_by_id(id)
        print("id =", plant["id"], plant["name"], ":", plant["location"])
    if flag == 4:
        id = int(input('Type id of plant which you want to delete: '))
        Plant.delete(id)
    if flag == 5:
        name = input("Type name of employee: ")
        email = input("Type email of employee: ")
        plant_id = int(input("Type id of plant: "))
        employee = Employee(name, email, plant_id)
        employee.save()
    if flag == 6:
        employees = Employee.get_all()
        for employee in employees:
            print("id =", employee["id"], employee["name"], ":", employee["email"])
    if flag == 7:
        id = int(input("Type id of plant: "))
        employee = Employee.get_by_id(id)
        print("id =", employee["id"], employee["name"], ":", employee["email"])
    if flag == 8:
        id = int(input('Type id of employee: '))
        Employee.delete(id)
