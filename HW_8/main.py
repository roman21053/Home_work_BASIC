from classes import Employee
from datetime import date
from decimal import Decimal
from decorator import timer

employees = [
    Employee(name="John", start_work=date(2022, 5, 20), rate=Decimal("11"), taxes=10),
    Employee(name="Alex", start_work=date(2022, 5, 1), rate=Decimal("50"), taxes=20),
    Employee(name="Kseniya", start_work=date(2022, 5, 10), rate=Decimal("50"), taxes=40),
    Employee(name="Valeriy", start_work=date(2022, 4, 20), rate=Decimal("60"), taxes=50),
    Employee(name="Vera", start_work=date(2019, 5, 20), rate=Decimal("99"), taxes=60),
    Employee(name="Suzanna", start_work=date(2021, 5, 20), rate=Decimal("20"), taxes=10),
    Employee(name="Gleb", start_work=date(2021, 5, 20), rate=Decimal("20"), taxes=10),
]


@timer("Show table")
def show_table():
    Employee.show_header()
    for employee in employees:
        employee.show_row()
        Employee.show_line()


@timer("Update table")
def update_table():
    new_rates = [12, 55, 52, 64, 95, 25, 30]
    new_rate = (new_rates[i] for i in range(len(new_rates)))
    for i in range(len(employees)):
        employees[i].update_rate(next(new_rate))


if __name__ == "__main__":
    show_table()
    update_table()
    show_table()
