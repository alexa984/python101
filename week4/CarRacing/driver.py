from car import Car
class Driver:
    def __init__(self, name, car):
        if type(car) == Car:
            self.name = name
            self.car = car
        else:
            raise TypeError()

    def __str__(self):
        return self.name + ' ' + str(self.car)