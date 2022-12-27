from datetime import date
from decimal import Decimal


class Employee:

    ROW_FORMAT = "| {:<30} | {:<10} | {:<10} | {:<10} |"
    ROW_LENGTH = 73

    def __init__(self, name: str, start_work: date, rate: Decimal, taxes: int, end_work: date = date.today()):
        self.validation(name=name, start_work=start_work, end_work=end_work, rate=rate, taxes=taxes)
        self._name = name
        self._start_work = start_work
        self._rate = rate
        self._taxes = taxes
        self._end_work = end_work
        self._balance = self._recalculate_balance()

    @staticmethod
    def validation(name: str, start_work: date, end_work: date, rate: Decimal, taxes: int):
        if end_work < start_work:
            raise ValueError("Start date can't be more than today")
        if not Decimal("100") > rate > Decimal("10"):
            raise ValueError("Rate must be between 10 and 100")
        if not 99 >= taxes > 1:
            raise ValueError("Taxes must be between 1 and 99")
        if not 20 >= len(name) >= 4:
            raise ValueError("Name must be from 4 to 20 characters")

    def days(self):
        return (self._end_work - self._start_work).days

    def how_long(self):
        return f"{self._name} works {self.days()} day(s)."

    def _recalculate_balance(self):
        self._balance = self._rate * self.days()
        return self._balance

    def update_rate(self, rate):
        self._rate = rate
        self._balance = self._recalculate_balance()
        return self._rate

    @property
    def rate(self):
        return self._rate

    @classmethod
    def show_header(cls):
        task = ["Name", "Balance ", "Taxes Pay", "Salary"]
        cls.show_line()
        print(cls.ROW_FORMAT.format(*task))
        cls.show_line()

    @classmethod
    def show_line(cls):
        print(cls.ROW_LENGTH * "-")

    def show_row(self):
        _name = self.how_long()
        _balance = self._balance
        _taxes_pay = self._taxes * self.days()
        _salary = self._balance - _taxes_pay
        data = [_name, _balance, _taxes_pay, _salary]
        print(self.ROW_FORMAT.format(*data))
