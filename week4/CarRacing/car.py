class Car:
    @accepts(str, str, int)
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return self.car + ' model ' + self.model + ' max speed: ' + str(self.max_speed)
