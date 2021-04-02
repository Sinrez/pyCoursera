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
        return f'{self.broad_color} {self.broad_grain} {self.broad_yeast} хлеба  '

class Wurst:
    'Колбасный цех'
    def __init__(self, wurst_type):
        self.wurst_type = wurst_type

    def get_wurst_meat(self):
        return self.wurst_type

    def __str__(self):
        return f'с {self.wurst_type}'

class Cheese:
    'Сырный класс'
    def __init__(self, cheese_type):
        self.cheese_type = cheese_type

    def get_cheese_type(self):
        return self.cheese_type

    def __str__(self):
        return f'с  {self.cheese_type}'

class Butter:
    'для масла'
    def __init__(self, butter_type):
         self.butter_type = butter_type

    def get_butter_type(self):
        return self.butter_type

    def __str__(self):
        return f'с {self.butter_type}'

class Sandwich():
    'класс Sandwich, который будет описывать сам бутерброд (из каких ингредиентов состоит, кто его сделал)'
    def __init__(self, bread, wurst, cheese, butter, maker):
        self.bread = bread
        self.wurst= wurst
        self.cheese = cheese
        self.butter = butter
        self.maker = maker

    def __str__(self):
        return f'бутер, сделаннный из {self.bread} {self.wurst} {self.cheese} {self.butter}. По рецепту повара {self.maker}'


class SandwichMaker():
    'класс SandwichMaker, который будет уметь делать бутерброды из переданных ему ингредиентов'
    def __init__(self, bread, wurst, cheese, butter, maker):
        self.bread = bread
        self.wurst= wurst
        self.cheese = cheese
        self.butter = butter
        self.maker = maker

    def __str__(self):
        sandwich = Sandwich(self.bread, self.wurst, self.cheese, self.butter, self.maker)
        return f'Готов  {sandwich.__str__()}'

if __name__ == "__main__":
    """ Инициализируйте несколько объектов объектов каждого типа (разные булки хлеба, разные добавки, несколько поваров)
    и создайте три разных бутерброда."""
    br_color_type = {
        1: 'черного',
        2: 'белого',
        3: 'серого'
    }
    br_grain_type = {
        1: 'ржаного',
        2: 'пшеничного'
    }
    br_yeast_type = {
        1: 'дрожжевого',
        2: 'бездрожжевого'
    }
    # fabric_buter = []

    wurst_types = {
        1: 'копченой колбасой',
        2: 'ветчиной'
    }

    cheese_types = {
        1: 'копченым сыром',
        2: 'классическим сыром'
    }

    butter_types = {
        1: 'обычным маслом',
        2: 'диетическим маслом'
    }

    makers = {
        1: 'Бутербродова',
        2: 'Мясоедова'
    }

    go_input = 'Y'
    while go_input != 'N':
        print('Готовим бутер')
        broad_color_in = int(input('Введите 1 - для выбора черного хлеба, 2 - белого, 3 - серного: '))
        if broad_color_in not in range(1,4):
            exit('Выбран неcуществующий пункт интерфейса! Перзапустите программу!')
        broad_grain_in = int(input('Введите 1 - для ржаного хлеба, 2 - для пшеничного: '))
        if broad_grain_in not in range(1,3):
            exit('Выбран неcуществующий пункт интерфейса! Перзапустите программу!')
        broad_yeast_in = int(input('Введите 1 - для дрожжевого хлеба, 2 - для бездрожжевого: '))
        if broad_yeast_in not in range(1, 3):
            exit('Выбран неcуществующий пункт интерфейса! Перзапустите программу!')
        wurst_type_in = int(input('Введите 1 - для копченой колбасы, 2 - для ветчины: '))
        if wurst_type_in not in range(1, 3):
            exit('Выбран неcуществующий пункт интерфейса! Перзапустите программу!')
        cheese_type_in = int(input('Введите 1 - для копченого сыра, 2 - для классического сыра: '))
        if cheese_type_in not in range(1, 3):
            exit('Выбран неcуществующий пункт интерфейса! Перзапустите программу!')
        butter_type_in = int(input('Введите 1 - обычное масло, 2 - диетическое: '))
        if butter_type_in not in range(1, 3):
            exit('Выбран неcуществующий пункт интерфейса! Перзапустите программу!')
        maker_in = int(input('По рецепту какого повара? Введите 1 -Бутербродов, 2 - Мясоедов: '))
        if maker_in not in range(1, 3):
            exit('Выбран неcуществующий пункт интерфейса! Перзапустите программу!')
        # sandwich_count_in = int(input('Введите число - сколько таких бутебродов сделать: '))
        # if sandwich_count_in <= 0:
        #     print('Число бутеров должно быть больше нуля! Перзапустите программу!')
        #     break
        bread = Bread(br_color_type[broad_color_in], br_grain_type[broad_grain_in], br_yeast_type[broad_yeast_in])
        wurst = Wurst(wurst_types[wurst_type_in])
        cheese = Cheese(cheese_types[cheese_type_in])
        butter = Butter(butter_types[butter_type_in])
        sandwichMaker = SandwichMaker(bread,wurst,cheese,butter,makers[maker_in])
        print(sandwichMaker.__str__())
        go_input = input('Сделать еще один бутер? Y/N? Q - для выхода: ').upper()
        if go_input == 'Q':
            exit('Спасибо за обращение. Если нужно приготовить бутер - запустите заново программу')







