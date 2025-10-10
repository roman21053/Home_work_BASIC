
# 1. Створіть клас Vehicle з атрибутами екземпляра max_speed та mileage та методами increase_speed, break_speed, mileage_info

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        pass

    def break_speed(self):
        pass

    def mileage_info(self):
        pass


# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle та матиме власний метод seating_capacity

class Bus(Vehicle):
    def seating_capacity(self):
        pass


# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
print("Task 3. Визначте, від якого класу успадковується клас Bus:", end='\n\t')

audit = issubclass(Bus, Vehicle)

print(f'Does the Bus class inherit from the Vehicle class? - {audit}', end='\n\n')


# 4. Створіть екземпляр Bus під назвою school_bus та визначте, чи є school_bus об'єктом класу Vehicle/Bus
print("Task 4. Створіть екземпляр Bus під назвою school_bus та визначте, чи є school_bus об'єктом класу Vehicle/Bus:", end='\n\t')

school_bus = Bus(80, 300)

print(f'is school_bus an object of class Vehicle? - {isinstance(school_bus, Vehicle)}', end='\n\t')
print(f'is school_bus an object of class Bus? - {isinstance(school_bus, Bus)}', end='\n')

print()

# 5. Створіть новий клас School з атрибутами екземпляра get_school_id та number_of_students та методами school_address, main_subject
        
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_addres(self):
        pass

    def main_subject(self):
        pass


# 6*. Створіть новий клас SchoolBus, який успадкує всі методи від School та Bus та матиме власний - bus_school_color

class SchoolBus(Scool, Bus):
    def __init__(self):
        pass

    def bus_school_color(self):
        pass

    
# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
# створіть із нього кортеж та використовуючи спільну змінну, викличте метод eat.
print("Task 7", end='\n\t')

class Bear:
    def eat(self):
        return 'The Bear eat berries'
    

class Wolf:
    def eat(self):
        return 'The Wolf eat meat'
    

bear = Bear()
wolf = Wolf()

k = (bear, wolf)

for elem in k:
    print(elem.eat(), end='\n\t')

print()

# 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу, лише коли population > 1500,
# інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього завдання магічні методи

class City:
    def __new__(cls, name, population):
        cls.name = name
        cls.population = population
        if population > 1500:
            return object().__new__(City)
        else:
            return "Your city is too small"

    def __init__(self, name, population):
        self.name = name
        self.population = population
        

my_city = City('Zhydachiv', 1200)
print(my_city)

