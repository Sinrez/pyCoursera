# задача из видео практики: угадать число пользователя от 1 до 1000

def find_ddt():
    left = 1
    right = 1000
    while True:
        current = (left+right)//2
        is_right = input(f'Ваше число:{current}?(Введите Д -да, Б- больше, М- меньше): ').lower()
        if is_right.lower() == 'д':
            print('Угадали!')
            break
        elif is_right=='б':
            left = current + 1
        else:
            right = current - 1

# 1. Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная,
# то длина первой части должна быть на один символ больше). Переставьте эти две части местами,
# результат запишите в новую строку и выведите на экран.
# При решении этой задачи нельзя пользоваться инструкцией if.

def strr_cutter():
    strr = input('Введите строку: ')
    if len(strr) % 2 == 0:
        res = strr[len(strr)//2:] + strr[:len(strr)//2]
    else:
        res = strr[len(strr) // 2+1:] + strr[:len(strr) // 2+1]
    print(res)


# 2. Дана строка. Получите новую строку, заменив в заданной строке все цифры 1 на слово one.
def strr_one():
    print(input('Введите строку: ').replace('1','one'))

# 3. Дана строка. Получите новую строку, вставив между двумя символами исходной строки символ *. Выведите полученную строку.

def str_star_var_1():
    strr = input('Введите строку: ')
    res = []
    for s in strr:
        res.append(s)
    print('*'.join(res))

def str_star_var_2():
    print(input('Введите строку: ').replace('','*')[1:-1])

# 4. Вводится число в десятичной системе счисления. Перевести его в римскую.

def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')

def to_roman():
    """Максимальное число, которое можно записать римскими цифрами,
    не нарушая правил Шварцмана (правил записи римских цифр) - 3999
    (MMMCMXCIX) - больше трех цифр подряд писать нельзя."""
    inp = input('Введите число: ')
    check_dgt(inp)
    inp = int(inp)
    if not 0 < inp < 4000:
        exit('Число должно быть от 0 до 4000')
    arab = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    rome = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i in range(len(arab)):
        count = int(inp / arab[i])
        result += rome[i] * count
        inp -= arab[i] * count
    print(result)

if __name__ == '__main__':
    # find_ddt()
    # strr_cutter()
    # strr_one()
    # str_star_var_1()
    # str_star_var_2()
    to_roman()