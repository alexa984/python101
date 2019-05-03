from random import sample
from driver import Driver
class Race:
    def __init__(self, drivers, crash_chance):
        if crash_chance < 0 or crash_chance > 1:
            raise ValueError()
        elif any([type(x) is not Driver for x in drivers]):
            raise TypeError()
        self.drivers = drivers
        self.crash_chance = crash_chance

    def result():
        racers_number = len(self.drivers)
        racers_to_crash = int(racers_number * self.crash_chance)
        drivers_sorted_by_fastest_cars = sorted(self.drivers, key = lambda x: x.car.max_speed, reverse = True)
        return delete_rand_items(drivers_sorted_by_fastest_cars, racers_to_crash)

    @staticmethod
    def delete_rand_items(items,n):
        to_delete = set(sample(range(len(items)),n))
        return [x for i,x in enumerate(items) if not i in to_delete]