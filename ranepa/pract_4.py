# #Общая функция проверки ввода
def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')
    if int(d) <= 99:
         exit('Нужно ввести натуральное число N>99')

# a Вводится натуральное число N>99. Функция возвращает число, получающееся отбрасыванием первой и последней цифры.
def digit_cutter(d):
    return (d[1: len(d)-1])

if __name__ == '__main__':
    n_in = input('Вводите натуральное число N>99: ').strip()
    check_dgt(n_in)
    print(digit_cutter(n_in))

# Вводится натуральное число N. Функция возвращает:
# 1. 1, если N простое число:
# 2. 0, если N составное число;
# 3. -1, если N=1.

#Общая функция проверки ввода
def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

def IsPrime(n):
    k = 2
    p = 0
    while k <= pow(n,0.5) and k > 1:
        if n % k == 0:
            p +=1
        k +=1
    return p == 0

def check_dgt(d):
    d = int(d)
    if d == 0:
        return '0 - не относится к простым или составным'
    elif d == 1:
        return -1
    elif IsPrime(d):
        return 1
    else:
        return 0

if __name__ == '__main__':
    n_in = input('Вводите натуральное число N: ').strip()
    check_dgt(n_in)
    print(check_dgt(n_in))

# с  В строке слова разделены хотя бы одним пробелом. Поменять местами слова минимальной и максимальной длины.

strr = input('Введите строку: ').split()
i = strr.index(min(strr, key=len))
j = strr.index(max(strr, key=len))
strr[i], strr[j] = strr[j], strr[i]
print(' '.join(strr))

# # d. В строке слова разделены хотя бы одним пробелом. Подсчитать, сколько раз заданное слово входит в строку.
strr = input('Введите строку: ').split()
wrd = input('Введите слово: ').strip()
count = 0
for s in strr:
    if s == wrd:
        count += 1
print(f'Слово {wrd} встречается {count} раз(а)')