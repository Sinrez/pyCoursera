class Mileage:
    def __init__(self, speed,car_mileage):
        self.speed = speed
        self.car_mileage = car_mileage
    def get_property_car(self):
        property_car = f'Максимальная скорость {self.speed}, пробег {self.car_mileage}'
        return property_car

benz = Mileage(200, 50000)
print(benz.get_property_car())
