class Person:
    def __init__(self, name, age, nationality, sex):
        self.name = name
        self.age = age
        self.nationals = nationality
        self.sex = sex
    
    def info(self):
       print(f'My name is {self.name}. I`m {self.nationals} and I`m {self.age} years old')


Anna = Person('Anna', 13, 'Ukrainian', 'female')

Anna.info()


class Student(Person):
    def __init__(self, name, age, nationality, sex, schol, grade):
        super().__init__(name, age, nationality, sex)
        self.__schol = schol
        self.grade = grade

    def student_info(self):
        self.info()
        print(f'I am in {self.grade} grade.')


Anna1 = Student('Anna', 13, 'Ukrainian', 'female', 'number 3', '7-Б')
Anna1.student_info()

print(issubclass(Student, Person))
print(isinstance(Anna1, Student))
print(Anna1._Student__schol)

print(Student.mro())
