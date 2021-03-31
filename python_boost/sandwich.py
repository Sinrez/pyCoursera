class Bread:
    'класс для описания свойств хлеба (черный, белый, зерновой и т.д.)'
    def __init__(self, broad_color, broad_grain, broad_yeast):
        self.broad_color = broad_color
        self.broad_grain = broad_grain
        self.broad_yeast = broad_yeast

    def get_broad_color(self):
        return self.broad_color

    def get_broad_grain(self):
        return self.broad_grain

    def get_broad_yeast(self):
        return self.broad_yeast

    def __str__(self):
        return self.broad_color + ' хлебом '+self.broad_grain +' '+self.broad_yeast

class Wurst:
    'Колбасный цех'
    def __init__(self, wurst_type):
        self.wurst_type = wurst_type

    def get_wurst_meat(self):
        return self.wurst_type

    def __str__(self):
        return 'с кобасой вида ' + self.wurst_type

class Cheese:
    'Сырный класс'
    def __init__(self, cheese_type):
        self.cheese_type = cheese_type

    def get_cheese_type(self):
        return self.cheese_type

    def __str__(self):
        return 'с сыром вида '+ self.cheese_type

class Butter:
    'для масла'
    def __init__(self, butter_type):
         self.butter_type = butter_type

    def get_butter_type(self):
        return self.butter_type

    def __str__(self):
        return 'с маслом типа '+self.butter_type

class Sandwich():
    'класс Sandwich, который будет описывать сам бутерброд (из каких ингредиентов состоит, кто его сделал)'
    def __init__(self, bread, wurst, cheese, butter, maker):
        self.bread = bread
        self.wurst= wurst
        self.cheese = cheese
        self.butter = butter
        self.maker = maker

    def __str__(self):
        return 'Бутер сделан из' + self.bread + self.wurst + self.cheese + self.butter + ' сделал ' + self.maker


class SandwichMaker():
    'класс SandwichMaker, который будет уметь делать бутерброды из переданных ему ингредиентов'
    def __init__(self, bread):
        self.bread = bread

    def set_bread(self,bread):
        self.bread = bread

    def __str__(self):
        return 'Изготовлен бутер с ' + self.bread.__str__()

if __name__ == "__main__":
    """ Инициализируйте несколько объектов объектов каждого типа (разные булки хлеба, разные добавки, несколько поваров)
    и создайте три разных бутерброда."""
    br_color_type = {
        1: 'черным',
        2: 'белым',
        3: 'серым'
    }
    br_grain_type = {
        1: 'ржаной',
        2: 'пшеничный'
    }
    br_yeast_type = {
        1: 'дрожжевой',
        2: 'бездрожжевой'
    }
    print('Готовим бутер')
    broad_color_in = int(input('Введите 1 - для выбора черного хлеба, 2 - белого, 3 - серного: ' ))
    broad_grain_in = int(input('Введите 1 - для ржаного хлеба, 2 - для пшеничного: '))
    broad_yeast_in = int(input('Введите 1 - для дрожжевого хлеба, 2 - для бездрожжевого: '))

    bread = Bread(br_color_type[broad_color_in],br_grain_type[broad_grain_in],br_yeast_type[broad_yeast_in])
    s_macker = SandwichMaker(bread)
    print(' ')
    print(s_macker.__str__())
    print('Я программа MVP -  пристрелите меня')

