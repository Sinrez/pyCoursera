class Coffee:
    def __init__(self, beans_volume, milk_volume, water_volume):
        self.beans_volume = beans_volume
        self.milk_volume = milk_volume
        self.water_volume = water_volume

class Coffee_machine:
    def __init__(self,coffee_class, cup_count):
         self.coffee_type = coffee_class
         self.cup_count = cup_count
         self.__water_limit = 2000
         self.__milk_limit = 1500
         self.__total_count = 0

    def set_coffee_type(self, coffee_type):
        self.coffee_type = coffee_type

    # def coffee_initializer(self):
    #     if self.coffee_type == 1:
    #         cappuccino = Coffee(50,100,100)
    #     else:
    #         espresso = Coffee(50,0,50)


    def set_total_count(self,cup_count):
        self.__total_count += cup_count

    def water_control(self):
        if self.__water_limit <= 300:
            print('Долейте воду!')

    def milk_control(self):
        if self.__milk_limit <= 200:
            print('Долейте молоко или выберите Эспрессо')




if __name__ == "__main__":
    change = int(input('Выберите вид кофе: 1 - Капучино, 2 - Эспрессо, 0 - завершить работу и выйти: '))
    if change in (1,2):
        cup_count = int(input('Введите количество кружек'))
        coffee_machine = Coffee_machine(change,cup_count)
        print(coffee_machine.result)
    elif change == 0:
        exit('Пока!')
    else:
        exit('Введено некорректное значние, запустите программу заново!')

