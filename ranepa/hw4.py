# # 1. Среди чисел от 1 до 200 выведите те,которые делятся на 7
# for i in range(1, 201):
#     if i % 7 == 0:
#         print(i)
#
# # 2. Вводится 10 чисел с клавиатуры. Найти среди них максимум и минимум. (не надо создавать 10 переменных! нужны циклы)
# dgts = []
# dgts_res = []
# for i in range(1, 11):
#     dgts.append(input(f'Введите {i} число: '))
# for d in dgts:
#     if not d.isdigit():
#         exit('В вашем вводе есть не числовые символы, повторите ввод.')
# for d in dgts:
#     dgts_res.append(int(d))
#
# print('---------------------')
# print(f'Максимум из ввода: {max(dgts_res)}')
# print(f'Минимум из ввода: {min(dgts_res)}')
#
# #вариант с циклом:
# n = 10
# i = 2
#
# numb = float(input("Введите число 1  число:"))
# minnum = numb
# maxnum = numb
#
# while i < n + 1:
#   numb = float(input(f'Введите {i} число: '))
#   if numb < minnum:
#     minnum = numb
#   if numb > maxnum:
#     maxnum = numb
#   i += 1
#
# print("Максимум из чисел = ", maxnum, "Минимум из чисел =", minnum)
#
# 3 Найти сумму тех цифр заданного натурального числа, которые делятся на 3
dgt_in = input("Введите число: ").strip()
if not dgt_in.isdigit():
    exit('Вы ввели не число, повторите ввод')

summ = 0
for d in dgt_in:
    if int(d) % 3 == 0:
        summ += int(d)

print(f"Сумма цифр числа {dgt_in}, которые делятся на 3: {summ}")
#
# # 4 Определите количество четных элементов в последовательности, завершающейся числом 0.
# num_even = -1
# element = -1
# print('Вводите последовательность чисел, для завершения ввода - введите 00, два нуля')
# while element != '00':
#     element = input('Введите число посдедовательности: ').strip()
#     if not element.isdigit():
#         exit('Вы ввели не число, повторите ввод')
#     elif int(element) % 2 == 0:
#         num_even += 1
# print(f'Кол-во элементов завершающейся числом 0: {num_even}')
#
# # 5 Последовательность состоит из различных натуральных чисел и завершается числом 0.
# # Определите значение максимального
# # элемента в этой последовательности.
# # Гарантируется, что в последовательности есть хотя бы два элемента.
#
# #Не совсем понятное условие, первый вар задачи, 5.1:
# sequence = input('Введите последовательность, "строку" чисел, завершающуюся нулем: ').strip()
# if not sequence.isdigit():
#     exit('В последовательности должны быть числа!')
# maxx = int(sequence[0])
# for s in sequence[1:]:
#     if int(s) >= int(maxx):
#         maxx = s
# print(f'Максимальный элемент последовательности {maxx}')
#
# #Второй вар задачи 5, 5.2:
# res = []
# print('Для завершения ввода ввести 0')
# while True:
#     dgt_inp = input('Введите натуральное число: ').strip()
#     if not dgt_inp.isdigit():
#         exit('Нужно ввести число!')
#     elif int(dgt_inp) != 0:
#         res.append(int(dgt_inp))
#     else:
#         break
# print(f'Максимальный элемент последовательности: {max(res)}')
#
# # 6 С клавиатуры вводится число n. Вычислить сумму S=1/1+1/2+1/3+...+1/n.
# n_inp = input('Введите число n: ').strip()
# if not n_inp.isdigit():
#     exit('Нужно ввести число!')
# n = int(n_inp)
# s = .0
# a = float
# for i in range(1, n + 1):
#     a = 1 / i
#     s = s + a
#     i = i + 1
# print(f'Сумма ряда равна {round(s,2)}')
#
# # 7 Вводится число n.Перевернутьего.12345 -> 54321
# #можно решить циклом с отрицательным шагом, но так быстрее:
# n_inp = input('Введите число: ').strip()
# if not n_inp.isdigit():
#     exit('Нужно ввести число!')
# print(f'Перевернутое число: {n_inp[::-1]}')
#
# # 8 С клавиатуры вводится число n.
# # Узнать, является ли n факториалом какого-либо числа?
# # Если да, то выведите это число (факториалом чего является n).
# n_inp = input('Введите число: ').strip()
# if not n_inp.isdigit():
#     exit('Нужно ввести число!')
# elif int(n_inp) == 1:
#     print(f'Число 1 является факториалом 0 или 1')
#     exit()
# dgt = int(n_inp)
# p = 1
# n = 1
# while p < dgt:
#     n += 1
#     p *= n
# if p == dgt:
#     print(f'Число {dgt} является факториалом числа {n}')
# else:
#     print(f'Число {dgt} не является факториалом')
#
# # 9 Найти 100-ое число Фибоначчи;
# fibo=[0,1]
# a=0
# b=1
# for i in range(0,98,1):
#     fibo.append(fibo[a]+fibo[b])
#     a+=1
#     b+=1
# print(f'100-ое число Фибоначчи: {fibo[99]}')
#
# # 10 Вычислить сумму первых N всех чисел Фибоначчи. N вводится с клавиатуры
# def fibo(n):
#     if n in [1,2]:
#         return 1
#     else:
#         res = fibo(n-1) + fibo(n-2)
#     return res
#
# def sum_fibo(n):
#     res = [fibo(i) for i in range(1, n+1)]
#     return sum(res)
#
# n_inp = input('Введите число: ').strip()
# if not n_inp.isdigit():
#     exit('Нужно ввести число!')
# n = int(n_inp)
#
# print(f'Сумма {n_inp} чисел Фибоначчи: {sum_fibo(n)}')

# 10 через циклы

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n_inp = input('Введите число: ').strip()
if not n_inp.isdigit():
    exit('Нужно ввести число!')

data = list(fibonacci(int(n_inp)))

print(f'Сумма {n_inp} чисел Фибоначчи: {sum(data)}')