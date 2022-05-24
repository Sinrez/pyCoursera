# Иногда, набор каких-то повторяющихся команд нужно выполнять несколько раз.
# Такие блоки команд обычно выносят в отдельные кусочки программы.
# Именно из функций состоят внешние модули, которые можно импортировать.
# В ООП функции являются методами класса и пишутся через точку от его названия.
# Для примера разберём простейшую функцию, назовем ее exfun
def exfun(a, b):
    c = a * b
    return c
    
a = 6
b = 5
c = exfun(a, b)
print(c)
print( exfun(2,2) + exfun(3,3) )

print('--------------')

# Мы можем задать один из параметров как необязательный,
# установив для него значение по умолчанию
# Необязательные параметры должны идти только после обязательных
def exfun2(d, e=10):
    f = d * e
    return f
    
print(exfun2(5))

# Несмотря на то, что b в данном случае равен по умолчанию 10,
# и не обязателен для передачи в качестве второго аргумента,
# мы по прежнему можем передавать второй аргумент, если захотим,
# и тогда в качестве b будет использовано не 10 переданный аргумент.
print(exfun2(2, 5))

print('--------------')

# Если функция должна возвращать больше чем одну переменную,
# то переменные можно писать через запятую
def getage(age):
    a = age - 18
    b = 73 - age
    return a, b
    
a, b = getage(33)
print('Вы уже взрослый: ', a, ' лет. Осталось жить примерно: ', b, ' лет')
 
print('--------------')
 
 # Функция, которая ничего не возвращает через return, вернет None
 
 # Внутри функций вы можете использовать переменные,
# которые встречались в коде программы до команды вызывающей функцию.
# Но если внутри кода функции после какой-то из переменных поставить знак =
# то эта переменная автоматически становится локальной,
# и все её дальнейшие изменения не выходят в основной код программы.

def boom():
    c = 100
    return c

c = 1
# Казалось бы сейчас вызовем функцию и с станет равно 100
# Но нет, это локальная с, видимая только внутри кода функции
x = boom()
print(c)

# Если мы все же хотим внутри функций присвоить значение
# какой-то внешней переменную в начале кода функции эту переменную
# нужно объявить как глобальную

def boom2():
    global c
    c = 100
    return c

c = 1
# Казалось бы сейчас вызовем функцию и с станет равно 100
# Но нет, это локальная с, видимая только внутри кода функции
x = boom2()
print(c)