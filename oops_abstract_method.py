from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):  # Abstract method
        pass

    @abstractmethod
    def stop(self):  # Abstract method
        pass

# Concrete class (inherits from Vehicle)
class Car(Vehicle):
    def start(self):
        print("Car is starting with key ignition.")

    def stop(self):
        print("Car is stopping with brakes.")

# Concrete class (inherits from Vehicle)
class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a self-start button.")

    def stop(self):
        print("Bike is stopping using disc brakes.")

# Creating objects
car = Car()
car.start()  # Output: Car is starting with key ignition.
car.stop()   # Output: Car is stopping with brakes.

bike = Bike()
bike.start()  # Output: Bike is starting with a self-start button.
bike.stop()   # Output: Bike is stopping using disc brakes.