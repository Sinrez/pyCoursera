import circle
import rectangle

AREA_CIRCLE_CHOISE = 1
CIRCUMFERENCE_CHOISE = 2
AREA_RECTANGLE_CHOISE = 3
PERIMETER_RECTANGLE_CHOISE = 4
QUIT_CHOICE = 5

def main():

    choise = 0

    while choise != QUIT_CHOICE:
        display_menu()

         #получить ввод пользователя
        choise = int(input('Введите вариант: '))

        if choise == AREA_CIRCLE_CHOISE:
            radius = float(input('Введите радиус круга: '))
            print('Площадь окружности равна', circle.area(radius))
        elif choise == CIRCUMFERENCE_CHOISE:
            radius = float(input('Введите радиус круга: '))
            print('Длина окружности равна', circle.circumference(radius))
        elif choise == AREA_RECTANGLE_CHOISE:
            width = float(input("Введите ширину прямоугольника: "))
            length = float(input("Введите длину прямоугольника: "))
            print('Площадь равна', rectangle.area(width,length))
        elif choise == PERIMETER_RECTANGLE_CHOISE:
            width = float(input("Введите ширину прямоугольника: "))
            length = float(input("Введите длину прямоугольника: "))
            print('Площадь равна', rectangle.perimeter(width, length))
        else:
            print('Ошибка: недопустимый выбор')

#показываем меню например
def display_menu():
    print('МЕНЮ')
    print(10 * '*')
    print('1 Площадь круга')
    print('2 Длина окружности')
    print('3 Площадь прямоугольника')
    print('4 Периметр прямоугольника')
    print('5 выход')
    print(10 * '*')

#вызов главной функции
main()

