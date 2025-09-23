


class Human():
    def __init__(self, sex, name, surname):
        self.sex = sex
        self.name = name
        self.surname = surname

class Nationale():
    def __init__(self, country):
        self.country = country


class Ukrainian(Human, Nationale):
    def __init__(self, sex, name, surname, country, city):
        Human.__init__(self, sex, name, surname)
        Nationale.__init__(self, country)
        self.city = city


print(Ukrainian.mro())
roman = Ukrainian(
    'man', 
    'Roman', 
    'Mereniuk', 
    'Ukreinian', 
    'Zhudachiv'
    )
print(roman.sex)

