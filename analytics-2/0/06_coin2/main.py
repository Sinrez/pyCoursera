import math

def check_coin():
    """Если выбрать точку на координатной плоскости, то можно увидеть,
       что проекции ее координат на оси x и y являются катетами прямоугольного треугольника.
       А гипотенуза этого прямоугольного треугольника как раз показывает расстояние от начала координат до точки.
       Таким образом, если длина  гипотенузы будет меньше радиуса круга,
       то точка будет принадлежать кругу; иначе она будет находится за его пределами."""
    print('Введите координаты монетки.')
    x = float(check_dgt('Введите координаты x или q для выхода: '))
    y = float(check_dgt('Введите координаты y или q для выхода: '))
    r = float(check_dgt('Введите радиус: '))

    hypotenuse = math.sqrt(x ** 2 + y ** 2)
    print()
    if hypotenuse <= r:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")

def check_dgt(in_msg):
    while True:
        count_debtor = input(in_msg).strip()
        if count_debtor.lower() == 'q':
            exit('Работа завершена.')
        elif count_debtor.isalpha() == True:
            print('Нужно ввести число!')
        else:
            return count_debtor

if __name__ == '__main__':
    check_coin()