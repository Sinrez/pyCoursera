# #Общая функция проверки ввода
def check_dgt_n(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')
    if int(d) <= 99:
         exit('Нужно ввести натуральное число N>99')

def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

# 1. Вводится натуральное число N>99.
# Функция возвращает число, получающееся отбрасыванием первой и последней цифры N.

def digit_cutter():
    n_in = input('Вводите натуральное число N>99: ').strip()
    check_dgt_n(n_in)
    print(n_in[1: len(n_in )-1])

# 2. Вводится натуральное число N>9.
# Функция возвращает число, получающееся заменой первой цифры N на 9, а последней на 0.
def change_dgt():
    d = input('Введите натуральное число > 9: ').strip()
    check_dgt(d)
    d_ch = int(d)
    if d_ch <= 9:
        exit('Число должно быть больше 9')
    print('9' + d[1:-1] + '0')

# 3. Вводится натуральное число N. Функция возвращает:
# 1, если N простое число:
# 0, если N составное число;
# -1, если N=1.

def IsPrime(n):
    k = 2
    p = 0
    while k <= pow(n,0.5) and k > 1:
        if n % k == 0:
            p +=1
        k +=1
    return p == 0

def check_pr():
    d = input('Введите натуральное число: ').strip()
    check_dgt(d)
    d = int(d)
    if d == 0:
        print('0 - не относится к простым или составным')
    elif d == 1:
        print(-1)
    elif IsPrime(d):
        print(1)
    else:
        print(0)

# 4. Вводятся натуральные числа A и B. (A<B). Функция печатает через пробел все простые на [A,B].
def print_prime():
    a = input('Введите число А: ').strip()
    check_dgt(a)
    b = input('Введите число B: ').strip()
    check_dgt(b)
    a = int(a)
    b = int(b)
    if a >= b:
        exit('Должно быть A<B')
    print(f'Простые на интервале от {a} до {b}:')
    for d in range(a, b+1):
        if IsPrime(d):
            print(d, end = ' ')

if __name__ == '__main__':
    digit_cutter()
    # check_pr()
    # change_dgt()
    # print_prime()
