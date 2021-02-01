import Automobile

class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        Automobile.__init__(self, make,model,make, model, mileage, price)
        self.__doors = doors

    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors