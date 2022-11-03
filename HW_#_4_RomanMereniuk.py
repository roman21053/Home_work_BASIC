
# 1. Створіть клас Vehicle з атрибутами екземпляра max_speed та mileage та методами increase_speed, break_speed, mileage_info
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
            print("increase_speed")

    def break_speed(self):
            print("break_speed")

    def mileage_info(self):
            print("mileage_info")
print()

# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle та матиме власний метод seating_capacity
class Bus(Vehicle):
    def seating_capacity(self):
            print("seating_capacity")
print()

# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
print("Task 3. Визначте, від якого класу успадковується клас Bus:")
print("Does the Bus class inherit from the Vehicle class?\n - ", issubclass(Bus, Vehicle))
print()

# 4. Створіть екземпляр Bus під назвою school_bus та визначте, чи є school_bus об'єктом класу Vehicle/Bus
print("Task 4. Створіть екземпляр Bus під назвою school_bus та визначте, чи є school_bus об'єктом класу Vehicle/Bus:")
school_bus = Bus(140, 600)
print("is 'school_bus' an object of the Vehicle class?\n - ", isinstance(school_bus, Vehicle))
print("is 'school_bus' an object of the Bus class?\n - ",isinstance(school_bus, Bus))
print()

# 5. Створіть новий клас School з атрибутами екземпляра get_school_id та number_of_students та методами school_address, main_subject
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_address(self):
        print("school address")

    def main_subject(self):
        print("main subject")
        
print()

# 6*. Створіть новий клас SchoolBus, який успадкує всі методи від School та Bus та матиме власний - bus_school_color
print("Task 6")
class SchoolBus(Bus, School):
    def __init__(self, get_school_id, number_of_students, color):
        super().__init__(get_school_id, number_of_students)
        self.color = color

    def bus_school_color(self):
        print(f"bus school color is {self.color}")

bus_color = SchoolBus(20, 30, 'red')
bus_color.bus_school_color()
print()

# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
# створіть із нього кортеж та використовуючи спільну змінну, викличте метод eat.
print("Task 7")
class Bear:
    def __init__(self, area_of_residence, fur_color, eats):
        self.area_of_residence = area_of_residence
        self.fur_color = fur_color
        self.eats = eats

    def eat(self):
        print(f"A bears eats {self.eats}")


class Wolf:
    def __init__(self, area_of_residence, fur_color, eats):
        self.area_of_residence = area_of_residence
        self.fur_color = fur_color
        self.eats = eats

    def eat(self):
        print(f"A wolfs eats {self.eats}")

white_bear = Bear("wood", "white", "all")
grey_wolf = Wolf("wood", "grey", "meat")

for animals_eat in (white_bear, grey_wolf):
    animals_eat.eat()
print()


#        Магічні методи:
# 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу, лише коли population > 1500,
# інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього завдання магічні методи
print("Task 8")
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


city = City("Lviv", 900000)
print(city.__dict__)