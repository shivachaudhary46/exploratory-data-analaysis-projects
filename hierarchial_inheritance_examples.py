#hierarchial inheritance examples 
class Vechile:

    def vechile_data(self):
        print(f"hi I am vechile")

class car(Vechile):

    def car_data(self):
        print(f"hi I am car")

class Bike(Vechile):

    def bike_data(self):
        print(f"hi I am bike")

bike1 = Bike()
bike1.bike_data()
bike1.vechile_data()

car1 = car()
car1.vechile_data()