from collections import namedtuple
import dataclasses

# 1. Make the class with composition.


class Tree:
    def __init__(self, height: float, leaf, fruit='not fruit'):
        self.height = {'height': height}
        self.leaf = {'leaf', leaf}
        self.fruit = {'fruit', fruit}


class Garden:
    def __init__(self, area: float):
        self.area = area
        self.apple_tree = Tree(3.7, 'rounded', 'apple')
        self.pear_tree = Tree(5, 'small and elongated', 'pear')


my_garden = Garden(5)


# 2. Make the class with aggregation


class Laptop:
    def __init__(self, brand):
        self.brand = brand


class Devices:
    def __init__(self, name, connection_type, connection_point):
        self.name = name
        self.connectio_type = connection_type
        self.connectio_point = connection_point


hp = Laptop('hp')
printer = Devices('printer', 'USB', hp)


# 3. Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
print("task 3.")


class Sum:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def add_nums(self):
        return self.x + self.y + self.z
    

suma = Sum(2, 3, 5)
print(suma.add_nums(), end='\n\n')

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
    max_visitors_num = 0

    def __init__(self):
        self.visitors_count = 0
        if self.visitors_count > self.max_visitors_num:
            self.visitors_count = self.max_visitors_num

    def __setattr__(self, name, value):
        if name == 'visitors_count':
            if value > self.max_visitors_num:
                self.visitors_count = self.max_visitors_num
            else:
                object.__setattr__(self, name, value)   
        else:
            object.__setattr__(self, name, value)  

            
Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count, end='\n\n')

# 6. Create dataclass with 7 fields - key (int), name (str), phone_number (str),
# address (str), email (str), birthday (str), age (int)


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int



# 7. Create the same class (6) but using NamedTuple

AddressBookDataClass = namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])


# 8.

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
        return (f"AddressBook(key='{self.key}', name='{self.name}', phone_number='{self.phone_number}', address='{self.address}', email='{self.email}', birthday= '{self.birthday}', age='{self.age}')")


# 9.
print("Task 9.")

class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"

Person.age = 40

print(Person.age, end='\n\n')

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


roman = Student(1, 'Roman')
roman.student_email = 'roman@gmail.com'

print(getattr(roman, 'student_email'), end='\n\n')