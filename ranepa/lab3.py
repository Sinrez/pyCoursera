from random import randint

# 1 Введите список чисел с клавиатуры до тех пор, пока не введете 0.
# Удалите из списка каждый третий элемент
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
print(f'Вы ввели список: {lst}')
del lst[2::3]
print(f'Удалили из списка каждый третий элемент: {lst}')

# 2 Поменять местами в списке две его половины.
# Например, из списка [1,2,3,4,5] получить список [3,4,5,1,2]
def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

lst = [int(a) for a in input('Введите числа списка через пробел, для завершения нажмите Enter: ').split() if not check_dgt(a)]
# a =[1,2,3,4,5]
b = len(lst) // 2
print(lst[b:] + lst[:b])

# 3 Создать случайный список из десяти чисел от -2 до 2. Заменить в нем все единицы на число 5.
res = []
y = 1
while y <= 10:
    res.append(randint(-2,2))
    y += 1
print(f'Исходный список: {res}')
for i in range(len(res)):
    if res[i] == 1:
        res[i] = 5
print(f'Cписок после замены: {res}')

# 4 Создать случайный список из десяти чисел от -2 до 2. Удалить в нем все единицы.
res = []
y = 1
while y <= 10:
    res.append(randint(-2,2))
    y += 1
print(f'Исходный список: {res}')
res.remove(1)
print(f'Cписок после удаления: {res}')

# 5 Создать случайный список из двадцати чисел от -5 до 5. Определить самый часто встречающийся элемент в нем
res = []
y = 1
while y <= 20:
    res.append(randint(-5,5))
    y += 1
print(f'Исходный список: {res}')
max = res[0]
max_count = res.count(max)
for el in res:
    if res.count(el)>max_count:
        max = el
    max_count =res.count(el)
print(f'Cамый часто встречающийся элемент: {max}')
