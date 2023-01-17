import logging
from models.controller import Controller

date_strftime_format = "%d-%b-%y %H:%M:%S"
message_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="logs/main.log", format=message_format, datefmt=date_strftime_format, encoding="UTF-8", level=logging.DEBUG)


while True:
    print(
        "\n1. Add new plant      3. Get all plants     5. Get plant by id      7. Delete plant by id\n"
        "2. Add new employee   4. Get all employees  6. Get employee by id   8. Delete employee by id\n"
    )

    logging.info('Menu printed!!!')

    try:
        flag = int(input("Choose: "))
    except ValueError as err:
        logging.error(err)
        print('You must enter to type number')
        continue

    if flag == 1:
        Controller.add_new_plant()
    if flag == 2:
        Controller.add_new_employee()
    if flag == 3:
        Controller.get_all_plants()
    if flag == 4:
        Controller.get_all_employee()
    if flag == 5:
        Controller.get_plant_by_id()
    if flag == 6:
        Controller.get_employee_by_id()
    if flag == 7:
        Controller.delete_plant_by_id()
    if flag == 8:
        Controller.delete_employee_by_id()
    if 1 < flag > 8:
        logging.error('entered a number outside the menu range: ' + str(flag))
        print('You must enter number in the menu range')
