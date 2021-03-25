class Mileage:
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage
    def get_mileage(self):
        property_car = f'Максимальная скорость {self.speed}, пробег {self.mileage}'
        return property_car

benz = Mileage(200, 50000)
print(benz.get_mileage())
