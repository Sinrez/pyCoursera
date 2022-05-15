# Модифицируйте.класс.Element,.сделав.атрибуты.name,
# .symbol.и.number.приват- ными..Определите.свойство.получателя.для.каждого.атрибута,.возвращающее. его.значение.

class Element:
    def __init__(self,name, symbol, number):
        self.__name = name
        self.__symbol  = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return self.name +' '+self.symbol +' '+str(self.number)

el1 = Element('Hydrogen', 'H', 1)

# print(el1.name)
# print(el1.number)

# Определите.три.класса:.Bear,.Rabbit.и.Octothorpe..
# Для.каждого.из.них.опре- делите.всего.один.метод.—.eats()..
# Он.должен.возвращать.значения.'berries'. (для.Bear),.'clover'.(для.Rabbit).или.'campers'
# .(для.Octothorpe)..Создайте. по.одному.объекту.каждого.класса.и.выведите.на.экран.то,.что.ест.указанное. животное.

class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()

# print(b.eats())
# print(r.eats())
# print(o.eats())

# Определите.три.класса:.Laser,.Claw.и.SmartPhone..
# Каждый.из.них.имеет.только. один.метод.—.does()..
# Он.возвращает.значения.'disintegrate'.(для.Laser),. 'crush'.(для.Claw).или.'ring'.(для.SmartPhone)..
# Далее.определите.класс.Robot,. который. содержит. по. одному. объекту. каждого. из. этих. классов..
# Определите. метод.does().для.класса.Robot,.который.выводит.на.экран.все,.что.делают.его. компоненты.

class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:

    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartPhone = SmartPhone()

    def does(self):
        print(f'Мой функционал: {self.laser.does()}, {self.claw.does()}, {self.smartPhone.does()}')

r = Robot()
r.does()

