from collections import namedtuple
import dataclasses

# 1. Make the class with composition.
# Cуть задуму в тому, що в class Laptop створено об'єкти з рекомендаціями ємності акумуляторних батарей
# для "ноутбуків" на базі class Battery. Коли я створюю об'єкт class Laptop і ввожу параметри ноубука, 
# то отримую рекомендації з підбору ємності акумуляторної батареї. Деталізації структури тут не робив.
print("task 1.")
class Laptop:
    def __init__(self, brand_of_laptop, screen_size):
        self.brand_of_laptop = print(brand_of_laptop)
        self.screen_size = print(f"{screen_size} inches")
        inch_14 = Battery("battery for 14 inch screen - ", 45)
        inch_15 = Battery("battery for 15 inch screen - ", 52)
        inch_17 = Battery("battery for 17 inch screen - ", 62)
        self.laptop = [f"{inch_14.text}{inch_14.battery_capacity} Wh",
                       f"{inch_15.text}{inch_15.battery_capacity} Wh", 
                       f"{inch_17.text}{inch_17.battery_capacity} Wh"
                       ]


class Battery:
    def __init__(self, text, battery_capacity: int):
        self.text = text
        self.battery_capacity = battery_capacity


laptop = Laptop("dell", 14)
print(laptop.laptop)
print()


# 2. Make the class with aggregation
# Cуть задуму в тому, що виводиться позначення нот для кожної налаштованої струни в гітарах з різною кількістю струн.
print("task 2.")


class Guitar:
    def __init__(self, producer, number_of_strings):
        self.producer = print(f"Guitar brand is - '{producer}'")
        self.number_of_strings = number_of_strings


class GuitarString:
    def __init__(self, string_number):
        self.string_number = string_number
        if self.string_number == 6:
            print("""
                A first string - note 'E'
                A second string - note 'B'
                A third string - note 'G'
                A fourth string - note 'D'
                A fifth string - note 'A'
                A sixth string - note 'E'
                """)
        elif self.string_number == 7:
            print("A first string - note 'd1'\
                \nA second string - note 'h'\
                \nA third string - note 'g'\
                \nA fourth string - note 'D'\
                \nA fifth string - note 'H'\
                \nA sixth string - note 'G'\
                \nA sixth string - note 'D'"
                  )
        else:
            print(f"I don't know {self.string_number} string guitar.")


strings = GuitarString(7)
guitar = Guitar("Maestro", strings)
print()


# 3. Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
print("task 3.")


class Calc:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add_nums(self):
        return self.x + self.y + self.z


addition = Calc(4, 5, 6)
print(addition.add_nums())
print()

# 4*.
print("task 4.")


class Pasta:
    """
    Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients та визначає інгридієнти атрибута екземпляра.
    Він повинен мати 2 методи:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """
    ingredients = ['bacon', 'parmesan', 'eggs']

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara (cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise (cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)
pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)
print()

# 5*.
print("task 5.")


class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitor_num = 0
    
    __slots__ = ('visitors_count')
       
    def __setattr__(self, key, value):
        if  value > Concert.max_visitor_num:
            object.__setattr__(self, key, Concert.max_visitor_num)
        else:
            object.__setattr__(self, key, value)          


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)


# 6. Create dataclass with 7 fields - key (int), name (str), phone_number (str),
# address (str), email (str), birthday (str), age (int)
print("task 6.")


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


roman = AddressBookDataClass(5, 'Roman', '0506512021', '**********', 'roman21053@gmail.com', 'already passed', 37)
print(roman.name)
print()

# 7. Create the same class (6) but using NamedTuple
print("task 7.")


AddresBookDataClass = namedtuple('AddresBookDataClass', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

roman_1 = AddresBookDataClass(2, 'roman', '0506512021', 'lviv', '@gmail.com', 'not soon', 37)
print(roman_1._asdict())
print(roman_1.key)
print(roman_1[1])

# додавання до NamedTuple ще одного атрибуту
print('# додавання до NamedTuple ще одного атрибуту')
AddresBookDataClass = namedtuple('AddresBookDataClass', AddresBookDataClass._fields + ('eye_colour',)) 

roman_2 = AddresBookDataClass(2, 'roman', '0506512021', 'lviv', '@gmail.com', 'not soon', 37, 'brown')
print(roman_2._asdict())
print(roman_2.eye_colour)
print()

print("Task 8.")


class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of [AddressBook]:
     AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
    """
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return(f"AddressBook(key={self.key}, name={self.name}, phone_number={self.phone_number}, address={self.address}, "
               f"email={self.email}, birthday={self.birthday}, age={self.age})"
               )


address = AddressBook(2, 'roman', '0506512021', 'Lviv', '@gmail.com', 'not soon', 37)

print(address)
print()

# 9.
print("Task 9.")


class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


roman = Person()
print(roman.age)
roman.age = 37
print(roman.age)
print()

# 10.
print("Task 10.")


class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student_email = Student(5, 'Roman')
student_email.email = '@.gmail.com'
print(student_email.__dict__)
print(getattr(student_email, 'email'))    
