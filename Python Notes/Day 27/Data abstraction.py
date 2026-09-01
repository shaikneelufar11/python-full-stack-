from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    # Abstract Method
    @abstractmethod
    def start(self):
        pass

    # Concrete Method
    def fuel_type(self):
        print("Vehicle uses fuel or electricity")


# Child Class
class Car(Vehicle):

    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):

    def start(self):
        print("Bike starts with self start button")


# Objects
car = Car()
bike = Bike()

car.start()
car.fuel_type()

bike.start()
bike.fuel_type()