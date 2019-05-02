import json
def main:
    with open('cars.json', 'r') as json_file:
        cars_data = json.load(json_file)


class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return self.car + ' model ' + self.model + ' max speed: ' + self.max_speed


class Driver:
    def __init__(self, name, car):
        if type(car) == Car:
            self.name = name
            self.car = car
        else:
            raise TypeError()

    def __str__(self):
        return name + ' ' + str(car)

class Race:
    def __init__(self, drivers, crash_chance):
        if crash_chance < 0 or crash_chance > 1:
            raise ValueError()
        elif any([type(x) is not Driver for x in drivers]):
            raise TypeError()
        self.drivers = drivers
        self.crash_chance = crash_chance

    def result():
        for driver in drivers:
            #to stuff based on cars speed   -> driver.car.max_speed
            pass

class Championship:
    def __init__(self, name, races_count):
        self.name = name
        self.races_count = races_count

    def top3(self):


