# 1 Создать кортеж чисел от 1 до n. n – вводится с клавиатуры
dgt_in = input("Введите число: ").strip()
if not dgt_in.isdigit():
    exit('Вы ввели не число, повторите ввод')
n = int(dgt_in)
res = []
for i in range(1, n + 1):
    res.append(i)
res_tup = tuple(res)
print(res_tup)

# 2 n – вводится с клавиатуры. Заполнить кортеж числами, введенными с клавиатуры (n штук введем)
# и проверить его на упорядоченность по возрастанию. 1 2 3 4 5 – ок, по возрастанию, 1 0 1 0 – не ок, не по возрастанию
def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

n = input('Введите размер кортежа - кол-во вводимых чисел: ').strip()
check_dgt(n)
dgts = []
res = 'Кортеж упорядочен по возрастанию'
for i in range(1, int(n) + 1):
    dgts.append(input(f'Введите {i}-е число кортежа: '))
for d in dgts:
    check_dgt(d)
ctg = tuple(dgts)
for i in range(len(ctg)-1):
    if ctg[i] > ctg[i+1]:
        res = 'Не упорядочен по возрастанию'
print(res)

# 3 Введите список чисел с клавиатуры до тех пор, пока не введете 0.
# Распечатайте элементы с четными индексами.
def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

lst = []
i = 1
while(True):
    d = input(f'Введите {i}-е число списка, для завершения 0: ').strip()
    check_dgt(d)
    if int(d) == 0:
        break
    lst.append(int(d))
    i += 1
for j in range(len(lst)):
    if j % 2 == 0:
        print(lst[j], end=' ')

# 4 Введите список чисел с клавиатуры до тех пор, пока не введете 0.
# Удалите из списка все элементы, находящиеся на нечетных позициях.

def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

lst = []
i = 1
while(True):
    d = input(f'Введите {i}-е число списка, для завершения 0: ').strip()
    check_dgt(d)
    if int(d) == 0:
        break
    lst.append(int(d))
    i += 1
print(f'Исходный список: {lst}')
for j in range(len(lst)):
    if j % 2 != 0:
       del lst[j]

print(f'Cписок после удаления: {lst}')

#5 Дан список L и число n. Сформируйте и верните новый список,
# содержащий номера позиций, на которых n находится в списке L.
# Пусть n=1, L=[1,2,1,3,1,1,4]. Ответ - [0,2,4,5]
def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

lst = [int(a) for a in input('Введите числа через пробел, для завершения нажмите Enter: ').split() if not check_dgt(a)]
# lst = [1,2,1,3,1,1,4]
n = input('Введите число n: ').strip()
check_dgt(n)
pos=[]
for i in range(len(lst)):
    if int(n) == lst[i]:
        pos.append(i)
print(pos)

# 6 Необходимо переставить соседние элементы в списке.
# Если элементов нечетное число,
# то последний элемент остается на своем месте. [1,2,3,4,5]à[2,1,4,3,5]
def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

lst = [int(a) for a in input('Введите числа через пробел, для завершения нажмите Enter: ').split() if not check_dgt(a)]
# lst = [1,2,3,4,5]
for i in range(1, len(lst), 2):
    lst[i - 1], lst[i] = lst[i], lst[i - 1]
print(' '.join([str(i) for i in lst]))

# 7 Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1], A[1] на место A[2], ...,
# последний элемент переходит на место A[0]). Было [1,2,3,4,5], стало [5,1,2,3,4]
def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

lst = [int(a) for a in input('Введите числа через пробел, для завершения нажмите Enter: ').split() if not check_dgt(a)]

for i in range(len(lst)):
 lst[-1],lst[i] = lst[i], lst[-1]
print(f'Сдвиг {lst}')