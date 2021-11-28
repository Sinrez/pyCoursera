# 1.	Определить является ли число простым. Попросить пользователя ввести произвольное целочисленное число.
# Вывести «Число простое», если число является простым и «Число не просто» в остальных случаях.
# Если пользователь вводит не число, то сообщить ему об этом и попросить ввести число еще раз.
# Ограничение на вводимое число: 0 < x < 100 000 000

def check_dgt(d):
    if not 0 < int(d) < 100000000:
        exit('Введено не целое число из интервала 0 < x < 100 000 000')

def IsPrime(n):
    n = int(n)
    k = 2
    p = 0
    while k <= pow(n, 0.5) and k > 1:
        if n % k == 0:
            p += 1
        k += 1
    return p == 0

def dgt_check_is_pr(d):
    if IsPrime(d):
        print('Число простое')
    else:
        print('Число не простое')

if __name__ == '__main__':
    dgt = input('Введите число: ').strip()
    check_dgt(dgt)
    dgt_check_is_pr(dgt)

# 2. Инвесторы: простые и сложные %

Anastasia = 100
Kate = 100
year = 1

while Kate <= Anastasia:
    Anastasia += 10
    Kate *= 1.05
    print(f'Год {year}')
    print('-' * 40)
    print(f'Вклад Анастасии: {Anastasia}')
    print("Вклад Екатерины:" '{:.2f}'.format(Kate))
    print('-' * 40)
    year += 1
print(f'Вклад Екатерины превысит вклад Анастасии через {year - 1} лет')

# 3.	Напишите программу, которая многократно запрашивает у пользователя пару чисел до тех пор,
# пока хотя бы одно из этой̆ пары не будет равно О. С каждой̆ парой̆ программа должна
# использовать функцию для вычисления среднего гармонического этих чисел.
# Среднее гармоническое чисел - это инверсия среднего значения их инверсий; она вычисляется следующим образом:
# среднее_гармоническое = 2• 0 х A x B / (A+B)

def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')


def harmonic_mean(x, y):
    return 2.0 * x * y / (x + y)


def get_harmonic_mean():
    while True:
        dgt1 = input('Введите первое число пары или 0 - для выхода: ').strip()
        dgt2 = input('Введите второе число пары или 0 - для выхода: ').strip()
        check_dgt(dgt1)
        check_dgt(dgt2)
        dgt1 = int(dgt1)
        dgt2 = int(dgt2)
        if dgt1 == 0 or dgt2 == 0:
            print('Введен 0 - выходим')
            break
        else:
            print('-' * 55)
            print(f'Среднее гармоническое {dgt1} и {dgt2} равно: ' '{:.2f}'.format(harmonic_mean(dgt1, dgt2)))
            print('-' * 55)


if __name__ == '__main__':
    get_harmonic_mean()