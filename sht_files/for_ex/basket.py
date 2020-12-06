import sys

values = sys.argv[1:]

# Список с результатом.
income = outcome = 0

# Запускаем цикл.
for value in values:
    value = int(value)

    # Распределяем по переменным.
    if value > 0:
        income += value
    else:
        outcome += value

# Вывод результата. Не забываем привести расходы к положительному числу.
print("Доходы: {} руб.\nРасходы: {} руб.".format(income, outcome * -1))