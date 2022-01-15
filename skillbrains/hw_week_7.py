# 1. Дан список L и число n.
# Сформируйте и верните новый список, содержащий номера позиций, на которых n находится в списке L.

def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

def input_list():
    lst = [int(a) for a in input('Введите числа через пробел, для завершения нажмите Enter: ').replace('', ' ').replace(',',' ').split() if
           not check_dgt(a)]
    return lst

def find_l():
    dgt = input('Введите число, которое ищем: ').strip()
    check_dgt(dgt)
    dgt = int(dgt)
    lst = input_list()
    print(*lst)
    res = []
    for i in range(len(lst)):
        if lst[i] == dgt:
            res.append(i)
    print(*res)

# 2. Необходимо переставить соседние элементы в списке. Если элементов нечетное число,
# то последний элемент остается на своем месте. Запрещается изменять размер исходного списка.
# Решите эту задачу одним оператором цикла, без использования if. [1,2,3,4,5]->[2,1,4,3,5]

def change_elem():
    lst = input_list()
    for i in range(1, len(lst), 2):
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
    print(' '.join([str(i) for i in lst]))

# 3. Циклически сдвиньте элементы списка вправо
# (A[0] переходит на место A[1], A[1] на место A[2], ..., последний элемент переходит на место A[0]).

def offset_elem():
    lst = input_list()
    for i in range(len(lst)):
        lst[-1], lst[i] = lst[i], lst[-1]
    print(f'Сдвиг {lst}')

if __name__ == '__main__':
    # find_l()
    # change_elem()
    offset_elem()
