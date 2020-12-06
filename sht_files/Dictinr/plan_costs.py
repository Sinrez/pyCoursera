import sys

# Получаем год.
year = int(sys.argv[1])

plans = {
    2017: [False, False, False, False, False, False, False, False, False, False, False, False],
    2018: [True, True, False, False, True, False, True, True, False, True, True, True],
    2019: [True, True, True, True, True, False, True, True, False, True, True, True],
    2020: [True, True, True, True, True, False, True, True, False, False, False, False],
    2021: [True, True, True, True, True, True, True, True, True, True, True, True]
}


# Вычисляем процент.
# Так как True - это синоним 1, то можно прсото сложить все значения списка.
percent = sum(plans[year]) * 100 / 12

# Выводим результат.
print("{:.0f}%".format(percent))