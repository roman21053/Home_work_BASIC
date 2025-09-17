import datetime


class Human:
    def __init__(self, name, surname, age, birth_day):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth_day = birth_day


class HumanSerializer:

    def serializer(self, obj, format):
        if format == 'csv':
            import csv
            with open('serializer/serializer.csv', 'a') as file:
                f = csv.writer(file)
                f.writerow(obj.birth_day)


obj = Human('Roman', 'Mereniuk', 37, datetime.date(1985, 8, 18))
format = "csv"




HumanSerializer(obj, 'csv') # 1985-08-18 => 18-08-1985
# HumanSerializer(obj, 'json') # 1985-08-18 => 1985-08-18 00:00:00
