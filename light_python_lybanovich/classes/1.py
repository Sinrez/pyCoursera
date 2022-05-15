# Создайте.класс.Thing,.не.имеющий.содержимого,.и.выведите.его.на.экран.
# # .Затем.создайте.объект.example.этого.класса.и.также.выведите.его..Совпада - ют.ли.выведенные.значения?

class Thing:
    pass

example = Thing()

# print(Thing)
# print(example)

# Создайте.новый.класс.с.именем.
# Thing2.и.присвойте.переменной.letters.зна- чение.'abc'..Выведите.на.экран.значение.letters.

class Thing2:
    letters = 'abc'

# print(Thing2.letters)

# Создайте.еще.один.класс,.который,.конечно.же,.называется.Thing3..В.этот.раз. присвойте.значение.'xyz'.атрибуту.
# объекта.letters..Выведите.на.экран.зна-
# Глава 10. Ой-ой-ой: объекты и классы 223 чение.атрибута.letters..Понадобилось.ли.вам.создавать.объект.класса,.чтобы.
# сделать.это?

class Thing3:
    def __init__(self):
        self.letters = 'xyz'

# print(Thing3.letters)

# Создайте.класс.Element,.имеющий.атрибуты.объекта.name,.symbol.и.number..
# Создайте.объект.этого.класса.со.значениями.'Hydrogen',.'H'.и.1.

class Element:
    def __init__(self,name, symbol, number):
        self.name = name
        self.symbol  = symbol
        self.number = number

    def __str__(self):
        return self.name +' '+self.symbol +' '+str(self.number)

el1 = Element('Hydrogen', 'H', 1)
# print(el1)

# Создайте.словарь.со.следующими.ключами.и.значениями:.'name':.'Hydrogen',. 'symbol':.'H',.'number':.1..
# Далее.создайте.объект.с.именем.hydrogen.класса. Element.с.помощью.этого.словаря.

dictt = {'name':'Hydrogen','symbol':'H', 'number':1}
hydrogen = Element(dictt['name'], dictt['symbol'], dictt['number'])
# print(hydrogen)

hydrogen2 = Element(**dictt)
# print(hydrogen)

# Для.класса.Element.определите.метод.с.именем.dump(),
# .который.выводит.на. экран.значения.атрибутов.объекта.(name,.symbol.и.number)..Создайте.объект.
# hydrogen.из.этого.нового.определения.и.используйте.метод.dump(),.чтобы.вы- вести.на.экран.его.атрибуты.







