from abc import abstractmethod, ABC

# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
"""Example:

for i in FibonacciNumbers(10):
    print(i)
0
1
1
2
3
5
8
13
21
34
55
"""

print("Task #1")


class FibonacciNumbers:
    def __init__(self, number: int):
        self.number = number
        self.counter = 1
        self.x = 0
        self.y = 1
        self.z = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter == 1:
            self.counter += 1
            return self.x
        if 1 < self.counter <= self.number:
            if self.x == 0:
                self.x = self.y
                self.y = self.z
                self.z = self.x + self.y
                self.counter += 1
                return self.x
            if self.x > 0:
                self.x = self.y
                self.y = self.z
                self.z = self.x + self.y
                self.counter += 1
                return self.x
        else:
            raise StopIteration    

for i in FibonacciNumbers(10):
    print(i, end=', ')

print(end='\n\n')

# 2.* Implement generator for Fibonacci numbers
print("Task #2")


def generator_Fibonacci(number):
    x, y = 0, 1
    for i in range(number + 1):
        if i == 1:
            yield x
        if i > 1:
            x, y = y, x + y
            yield x


for i in generator_Fibonacci(7):
    print(i, end=', ')

print(end='\n\n')

# 3. Write generator expression that returns square numbers of integers from 0 to 10
print("Task #3")

gen_square_numbers = [i ** 2 for i in range(11)]

for i in gen_square_numbers:
    print(i, end=', ')

print(end='\n\n')

# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.


class Laptop(ABC):
    
    @abstractmethod
    def Screen(self):
        raise NotImplementedError
    
    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError
    
    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError
    
    @abstractmethod
    def WebCam(self):
        raise NotImplementedError
    
    @abstractmethod
    def Ports(self):
        raise NotImplementedError
    
    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError


class HpLaptop(Laptop):
    
    def Screen(self):
        print('Screen')
    
    def Keyboard(self):
        print('Keyboard')
    
    def Touchpad(self):
        print('Touchpad')
    
    def WebCam(self):
        print('WebCam')
    
    def Ports(self):
        print('Ports')
    
    def Dynamics(self):
        print('Dynamics')
    

# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.


class Car(ABC):

    def drive(self):
        print('drive')

    def stop(self):
        print('stop')
    
    @abstractmethod
    def open_door(self):
        raise NotImplementedError
    
    @abstractmethod
    def close_door(self):
        raise NotImplementedError
    
    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError
    
    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError
    
    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError
    
    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError
    