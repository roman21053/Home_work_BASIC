from models.controller import Controller

while True:
    print(
        "\n1. Add new plant      4. Get all plants     7. Get plant by id      10. Delete plant by id\n"
        "2. Add new employee   5. Get all employees  8. Get employee by id   11. Delete employee by id\n"
        "3. Add new salon      6. Get all salons     9. Get salon by id      12. Delete salon by id\n"
    )
    flag = int(input("Choose: "))
    if flag == 1:
        Controller.add_new_plant()
    if flag == 2:
        Controller.add_new_employee()
    if flag == 3:
        Controller.add_new_salon()
    if flag == 4:
        Controller.get_all_plants()
    if flag == 5:
        Controller.get_all_employee()
    if flag == 6:
        Controller.get_all_salons()
    if flag == 7:
        Controller.get_plant_by_id()
    if flag == 8:
        Controller.get_employee_by_id()
    if flag == 9:
        Controller.get_salon_by_id()
    if flag == 10:
        Controller.delete_plant_by_id()
    if flag == 11:
        Controller.delete_employee_by_id()
    if flag == 12:
        Controller.delete_salon_by_id()
