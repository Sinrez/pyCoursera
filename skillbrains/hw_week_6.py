# 1. Создать кортеж чисел от 1 до n.
# Заполнить кортеж числами с клавиатуры и проверить его на упорядоченность по возрастанию

def check_dgt(d):
    if not d.isdigit():
        exit('Вы ввели не число, повторите ввод')

def make_tuple():
    n = input('Введите число n элементов кортежа: ')
    check_dgt(n)
    n = int(n)
    res = []
    for i in range(1, n+1):
        d = input('Введите число: ')
        check_dgt(d)
        res.append(int(d))
    tup = tuple(res)
    return tup

def is_sort_tup(tup):
    res = 'Отсортирован по возрастанию'
    for i in range(1,len(tup)):
        if tup[i-1] > tup[i]:
            res = 'Неотсортирован'
            break
    print(7 * '-')
    print(res)
    print(7 * '-')
    print(tup)

# 2. Введите список с клавиатуры до 0. Распечатайте элементы с четными индексами. Пользоваться if нельзя.
def lst_even():
    print(list(input('Введите элементы списка без пробелов: ').strip().replace(' ',''))[::2])

# 3. Введите список через пробел. Удалите из списка все элементы, находящиеся на нечетных позициях
def lst_not_even():
    lst = input('Введите элементы списка через пробел: ').split(' ')
    for i,l in enumerate(lst):
        if i % 2 != 0:
            del lst[i]
    print(lst)

if __name__ == '__main__':
    # is_sort_tup(make_tuple())
    # lst_even()
    lst_not_even()