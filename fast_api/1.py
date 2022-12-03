import os
# Создаём цикл, чтобы вывести все переменные среды
print("The keys and values of all environment variables:")
for key in os.environ:
    print(key, '=>', os.environ[key])
# Выводим значение одной переменной
print("The value of HOME is: ", os.environ['HOME'])