import math
# 1. а) Напишите функцию Len, вычисляющую длину отрезка по координатам его концов.
#     В эту функцию передается 4 целых числа – координаты точек.

def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

def lenn(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

#    b)Вторая функция данной программы – square.
#     Она вычисляет площадь треугольника по формуле Герона.
#     В эту функцию передаются 6 целых чисел – координат x1, y1, x2, y2, x3, y3 вершин треугольника.
#     Она должна использовать функцию Len.

def square(x1, y1, x2, y2, x3, y3):
    check_dgt(x1)
    check_dgt(y1)
    check_dgt(x2)
    check_dgt(y2)
    check_dgt(x3)
    check_dgt(y3)
    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    y1 = int(y1)
    y2 = int(y2)
    y3 = int(y3)

    side_a = lenn(x1, y1, x2, y2)
    side_b = lenn(x1, y1, x3, y3)
    side_c = lenn(x2, y2, x3, y3)

    p = (side_a + side_b + side_c) / 3

    sq = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))

    print(round(sq,6))

# 2. С помощью функций напечатайте таблицу умножения (непонятно - с помощью каких именно функций)

def mult():
    for i in range(1, 11):
        print(' '.join(str(i * v) for v in range(1, 11)))

#    c) Все данные вводятся в основной программе. Вызовите в ней функцию square.
#    Ответ выведите с точностью до 6 знаков после десятичной точки, отведя под него 10 позиций.
if __name__ == '__main__':
    # x1 = input('Введите координату x1: ').strip()
    # y1 = input('Введите координату y1: ').strip()
    # x2 = input('Введите координату x2: ').strip()
    # y2 = input('Введите координату y2: ').strip()
    # x3 = input('Введите координату x3: ').strip()
    # y3 = input('Введите координату y3: ').strip()
    # square(x1, y1, x2, y2, x3, y3)
    mult()
