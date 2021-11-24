def function():
    print(1)

def f2(c):
    print(c)

def A():
    print()  
def B():
    A() 
def C():
    B()

function()

a = 10
b = 2

function()
# function(444)

f2(555)
f2(111)
# f2(1,2,3)




def f2(c):
    a = 10
    c += 100
    print(c)

f2(555)
f2(111)
# f2(1,2,3)
a = 1
f2(1000)
print(a)

b = 20
f2(b)

a = 1
f2(a)



# написать функцию, которая может посчитать факториал числа n

def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print(f)

fact(3)
fact(5)
fact(10)

# create_tab(10)
# create_field_address()
# create_app()



# написать функцию, которая может посчитать факториал числа n

def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i

    print(f)
    # return None

def fact2(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i

    return f

def fact3(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i

    print(f)
    return f

fact(3)
print(3)

a = int(3.4)
c = input()
b = fact2(3)
print(a, b, c)


q = fact(5)
print(q)

fact2(10)

# Алгоритм Евклида, нахождение Наибольшего Общего Делителя

def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        print(a, b)
    print("Answer: ", a)

c = int(input())
d = int(input())
gcd(c, d)





# Просуммировать элементы вида: 
# 1/1!, 1/2!, 1/3! ... 1/N!

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def sum(n):
    s = 0
    for i in range(1, n + 1):
        f = factorial(i)
        s += 1 / f
    return s

n = int(input())
result = sum(n)
print(result)




# Просуммировать элементы вида: 
# 100*1! + 4, 100*2! + 4, 100*N! + 4
# 100 * (1! + 2! + N!) + 4*N

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def sum(n):
    s = 0
    for i in range(1, n + 1):
        f = factorial(i)
        s += 100 * f + 4
    return s

n = int(input())
result = sum(n)
print(result)


# Просуммировать элементы вида: 
# 100*1! + 4, 100*2! + 4, 100*N! + 4
# 100 * (1! + 2! + N!) + 4*N

def func(a):
    return 100 * a + 4

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def sum(n):
    s = 0
    for i in range(1, n + 1):
        f = factorial(i)
        s += func(f)
    return s

n = int(input())
result = sum(n)
print(result)







from random import *
a = randint(-10, 10)
print(a)

import random
a = random.randint(-10, 10)
print(a)



import math

a = math.sqrt(400)
print(a)

k = 3.27
print(math.floor(k))
print(math.ceil(k))
print(math.trunc(k))
print(math.trunc(-4.123))

print(abs(-4.5))
print(math.fabs(-4.123))

print(math.pi)



# Напишите функцию, в которую поступает число N, и которая возвращает количество цифр в этом числе

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(count_digits(11233))


# Напишите функцию, в которую поступает число N, и которая возвращает сумму цифр в этом числе

def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

print(sum_digits(456))



# С помощью функций напечатайте таблицу умножения

def column_multiply(k):
    for i in range(1, 11):
        print(k, 'x', i, '=', k * i)

for i in range(2, 10):
    column_multiply(i)
    print()


# Вводится натуральное число N. Функция возвращает сумму делителей числа N.


def sum_of_dividers(N):
    s = 0
    for i in range(1, N + 1):
        if N % i == 0:
            s += i
            print(i)
    print()
    return s

n = int(input())
print(sum_of_dividers(n))



# В строке слова разделены хотя бы одним пробелом.
# • а) Подсчитать количество слов.

def count_words(string):
    return len(string.split())

s = input()
print(count_words(s))



# В строке слова разделены хотя бы одним пробелом.
# • а) Подсчитать количество слов.

def count_words(string):
    if string == '':
        return 0
    
    count = 1
    for i in range(len(string)):
        if string[i] == ' ':
            count += 1
    return count

s = input()
print(count_words(s))


# В строке слова разделены хотя бы одним пробелом.
# Подсчитать, сколько слов начинается с большой буквы.

def count_Upper_words(string):
    L = string.split()
    count = 0
    for i in range(len(L)):
        if L[i][0].isupper():
            count += 1
    return count

s = input()
print(count_Upper_words(s))










