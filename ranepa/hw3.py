import math

# # 1.Даны три целых числа. Выведите значение наименьшего из них.
dgt1 = int(input('Введите 1 число: '))
dgt2 = int(input('Введите 2 число: '))
dgt3 = int(input('Введите 3 число: '))
#
# # быстрый вар:
# # print(min(min(dgt1, dgt2), dgt3))
#
def min_dgt(dgt1, dgt2, dgt3):
    minn = dgt1
    if dgt2 < minn and dgt2 < dgt3:
        minn = dgt2
    elif dgt3 < minn and dgt3 < dgt2:
        minn = dgt3
    return minn

print(min_dgt(dgt1, dgt2, dgt3))

# 2. Два прямоугольника заданы длинами сторон. Определить, можно ли один из них полностью разместть внутри другого
side_a1 = int(input('Введите 1 сторону 1 прямоугольника: '))
side_b1 = int(input('Введите 2 сторону 1 прямоугольника: '))
side_a2 = int(input('Введите 1 сторону 2 прямоугольника: '))
side_b2 = int(input('Введите 2 сторону 2 прямоугольника: '))

# # тут что-то разные алгоритмы попадаются
# # взял отсюда https://progi.pro/obnaruzhit-esli-odin-pryamougolnik-mozhno-pomestit-v-drugoy-pryamougolnik-1428052
if side_a1 > side_b1:
    side_a1, side_b1 = side_b1, side_a1
if side_a2 > side_b2:
    side_a2, side_b2 = side_b2, side_a2

if side_a1 <= side_a2 and side_b1 <= side_b2:
    p = side_a1
    q = side_b1
    a = side_a2
    b = side_b2
elif side_a1 >= side_a2 and side_b1 >= side_b2:
    p = side_a2
    q = side_b2
    a = side_a1
    b = side_b1

if (p <= a and q <= b) or (
        p > a and b >= (2 * p * q * a + (p * p - q * q) * math.sqrt(p * p + q * q - a * a)) / (p * p + q * q)):
    print('Первый прямоугольник помещается во второй')
else:
    print('Первый прямоугольник не помещается во второй')

# 3 Про шарики:
count = int(input('Введите кол-во шариков: '))
if count % 3 == 0 or count % 5 == 0 or count % 3 == 2 or count % 5 == 3:
    print('Можно')
elif count >= 6 and (count - 6) % 5 == 0:
    print('Можно')
elif count >= 9 and (count - 9) % 5 == 0:
    print('Можно')
elif count >= 12 and (count - 12) % 5 == 0:
    print('Можно')
elif count <= 4:
    print('Нельзя')
else:
    print('Нельзя')

# 4. Даны три целых числа, записанных в отдельных строках. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадают) или 0 (если все числа различны).
dgt1 = int(input('Введите 1 число: '))
dgt2 = int(input('Введите 2 число: '))
dgt3 = int(input('Введите 3 число: '))
if dgt1 == dgt2 == dgt3:
    print(3)
elif dgt1 == dgt2 or dgt2 == dgt3 or dgt1 == dgt3:
    print(2)
else:
    print(0)

# 5 Таблица умножения
digit1 = input('Введите 1 целое однозначное число: ')
digit2 = input('Введите 2 целое однозначное число: ')
if digit1.isdigit() and digit2.isdigit():
    dgt1 = int(digit1)
    dgt2 = int(digit2)
else:
    exit('Вы ввели не целое однозначное число')
if not(0 <= dgt1 <= 9) or not(0 <= dgt2 <= 9):
    exit('Введено не однозначное число')

res = dgt1 * dgt2
answ = input(f'Результат умножения первого числа {dgt1} на второе {dgt2}? Введите: ')
if not answ.isdigit():
    exit('Вы ввели не число, повторите попытку заново!')
elif res == int(answ):
        print(f'Вы ответили {int(answ)} и это правильно!')
else:
    print(f'Вы ответили {int(answ)} и это неправильно, верный ответ: {res}')

#6 Шахматный слон ходит по диагонали.
# Даны две различные клетки шахматной доски,
# определите, может ли слон попасть с первой клетки на вторую одним ходом.

x1 = int(input('Введите координату x первой клетки: '))
y1 = int(input('Введите координату y первой клетки: '))
x2 = int(input('Введите координату x второй клетки: '))
y2 = int(input('Введите координату y второй клетки: '))
if abs(x1 - x2) == abs(y1 - y2):
    print('Может попасть')
else:
    print('Не может попасть')

#7 Шахматный конь

x1 = int(input('Введите координату x первой клетки: '))
y1 = int(input('Введите координату y первой клетки: '))
x2 = int(input('Введите координату x второй клетки: '))
y2 = int(input('Введите координату y второй клетки: '))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('Может попасть')
else:
    print('Не может попасть')

