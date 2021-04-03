class Coffee:
    def __init__(self, beans_volume, water_volume, milk_volume, coffee_volume):
        self.beans_volume = beans_volume
        self.water_volume = water_volume
        self.milk_volume = milk_volume
        self.coffee_volume =coffee_volume

    def __str__(self):
        return f'кофе'

class Coffee_machine:
    def __init__(self,coffee_type,coffee_volume, cup_count):
         self.coffee_type = coffee_type
         self.coffee_volume_ml = coffee_volume
         self.cup_count = cup_count
         self.__water_limit_ml = 2000
         self.__milk_limit_ml = 1500
         self.__beans_limit_mg = 9000
         self.__total_count = 0
         self.__beans_volume_mg = 50
         self.__water_volume_cuph_ml = self.coffee_volume_ml - self.__beans_volume_mg
         self.__milk_volume_mg = 100
         self.__water_volume_esppr_ml = 0

    def coffee_initializer(self):
        i =0
        while i < self.cup_count:
            if self.coffee_type == 1:
                print(f'Приготовлен {Coffee(self.__beans_volume_mg,self.__water_volume_cuph_ml,self.__milk_volume_mg, self.coffee_volume_ml)} эспрессо объемом {self.coffee_volume_ml}  порция номер {i +1}')
                self.__water_limit_ml -= self.__water_volume_cuph_ml
                if self.__water_limit_ml <= 300:
                    exit('Остаток воды меньше 300 мл, долейте воду и перезапустите программу!')
                self.__beans_limit_mg -= self.__beans_volume_mg
                if self.__beans_limit_mg <= 300:
                    exit('Остаток кофейных зерен меньше 300 мг, доспьте зерна и перезапустите программу!')
            if self.coffee_type == 2:
                print(f'Приготовлен {Coffee(self.__beans_volume_mg,self.__water_volume_esppr_ml,self.__milk_volume_mg,self.coffee_volume_ml)} капучино объемом {self.coffee_volume_ml} порция номер {i + 1}')
                self.__water_limit_ml -= self.__water_volume_cuph_ml
                if self.__water_limit_ml <= 300:
                    exit('Остаток воды меньше 300 мл, долейте воду и перезапустите программу!')
                self.__beans_limit_mg -= self.__beans_volume_mg
                if self.__beans_limit_mg <= 300:
                    exit('Остаток кофейных зерен меньше 300 мг, доспьте зерна и перезапустите программу!')
                self.__milk_limit_ml -= self.__milk_volume_mg
                if self.__milk_limit_ml <= 200:
                    exit('Остаток молока меньше 200 мл, долейте молоко и перезпустите программу!')
            i += 1

    def water_control(self):
        if self.__water_limit_ml <= 300:
            print('Долейте воду!')
        else:
            print(f'Остаток воды: {self.__water_limit_ml}')

    def milk_control(self):
        if self.__milk_limit_ml <= 200:
            print('Долейте молоко или выберите Эспрессо')
        else:
            print(f'Остаток молока: {self.__milk_limit_ml}')

    def beans_control(self):
        if self.__beans_limit_mg <= 300:
            print('Остаток кофейных зерен меньше 300 мг')
        else:
            print(f'Остаток кофейных зерен: {self.__beans_limit_mg}')


if __name__ == "__main__":
    volume_esppr_1 = 50
    volume_esppr_2 = 100
    volume_cupch_1 = 200
    volume_cupch_2 = 300
    change = int(input('Выберите вид кофе: 1 - Эспрессо, 2 - Капучино, 0 - завершить работу и выйти: '))
    if change == 1:
        coffee_volume = int(input('Введите объем кофе: 50 мл или 100 мл: '))
        if coffee_volume not in (volume_esppr_1,volume_esppr_2):
            exit('Введен некорректный объем кофе - перезапустите программу!')
        cup_count = int(input('Введите количество кружек: '))
        coffee_machine = Coffee_machine(change,coffee_volume, cup_count)
        coffee_machine.coffee_initializer()
        coffee_machine.water_control()
        coffee_machine.beans_control()
    elif change == 2:
        coffee_volume = int(input('Введите объем кофе: 200 мл или 300 мл: '))
        if coffee_volume not in (volume_cupch_1, volume_cupch_2):
            exit('Введен некорректный объем кофе - перезапустите программу!')
        cup_count = int(input('Введите количество кружек: '))
        coffee_machine = Coffee_machine(change,coffee_volume, cup_count)
        coffee_machine.coffee_initializer()
        coffee_machine.water_control()
        coffee_machine.milk_control()
        coffee_machine.beans_control()
    elif change == 0:
        exit('Пока!')
    else:
        exit('Введено некорректное значние, запустите программу заново!')

