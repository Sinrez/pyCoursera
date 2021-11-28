# • В математике функция sign(x) (знак числа) определена так: sign(x) = 1, если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) = 0, если x = 0.
# Напишите эту функцию

def check_dgt(d):
    if d.isalpha():
        exit('Вы ввели не число, повторите ввод')


def sign(x):
    check_dgt(x)
    x = float(x)
    res = 0
    if x > 0:
        res = 1
    elif x < 0:
        res = -1
    return res


if __name__ == '__main__':
    dgt = input('Введите число: ').strip()
    print(sign(dgt))


# Вводятся натуральные числа A и B. (A<B).
# Функция печатает через пробел все простые на отрезке [A,B].

def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не натуральное число, повторите ввод')


def IsPrime(n):
    k = 2
    p = 0
    while k <= pow(n, 0.5) and k > 1:
        if n % k == 0:
            p += 1
        k += 1
    return p == 0


def dgt_segment(a, b):
    check_dgt(a)
    check_dgt(b)
    a = int(a)
    b = int(b)
    if a >= b:
        exit('Первое число а должно быть больше второго числа b!')
    res = []
    for r in range(a, b + 1):
        if IsPrime(r):
            res.append(r)
    return ', '.join(map(str, res))


if __name__ == '__main__':
    dgt1 = input('Введите первое число а: ').strip()
    dgt2 = input('Введите второе число b: ').strip()
    print(dgt_segment(dgt1, dgt2))


# Написать функцию, в которую передается число N.
# В ней необходимо ввести N чисел.
# Вернуть надо минимум и максимум последовательности.

def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')


def make_digits(n):
    check_dgt(n)
    n = int(n)
    res = []
    for i in range(1, n + 1):
        try:
            res.append(int(input(f'Введите {i}-е число: ').strip()))
        except ValueError:
            print('Введено не число. Пропускаем.')
        except Exception:
            exit('Случилась системная ошибка')

    max_d = max(res)
    min_d = min(res)
    print('------------------------------')
    print(f'Максимум из введенных: {max_d}')
    print(f'Максимум из введенных: {min_d}')
    print('------------------------------')


if __name__ == '__main__':
    n = input('Введите размер последовательности чисел n: ').strip()
    check_dgt(n)
    print('------------------------------')
    make_digits(n)


# Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться склейка строк.
# В остальных случаях введенные числа суммируются.

def univers_sum():
    val1 = input('Введите первое значение: ').strip()
    val2 = input('Введите второе значение: ').strip()
    if not val1.isdigit() or not val2.isdigit():
        print(f'Склейка: {val1 + val2}')
    else:
        print(f'Сумма: {int(val1) + int(val2)}')


if __name__ == '__main__':
    univers_sum()
