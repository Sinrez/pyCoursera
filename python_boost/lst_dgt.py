# 8. Напишите программу, которая выводит чётные
# числа из заданного списка и останавливается, если встречает число 237.
lst = [2,3,4,5,7,7,88,8,237,2,4]
for i in lst:
    if i == 237:
        break
    elif i % 2 == 0:
        print(i)

