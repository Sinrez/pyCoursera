import json

# В качестве значения в словарях можно использовать другие словари
# Что позволет создавать сложные вложенные структуры данных

dict1 = {}

# Три раза попросим юзера ввести информацию о людях
for x in range(3):
    # Второй словарь
    dict2 = {}
    # В качестве ключа к первому словарю используем login
    login = input('Введите уникальный логин: ')
    # Остальными значениями заполним второй словарь
    dict2['name'] = input('Введите имя: ')
    dict2['age'] = input('Введите возраст: ')
    dict2['sex'] =  input('Введите пол: ')
    dict2['work'] = input('Введите должность: ')
    # Запишем второй словарь в качестве значения в первый
    dict1[login]=dict2
    print('---')
    
# Сохраним в файл
jsonData = json.dumps(dict1)
with open("peoples.json", "w", encoding='UTF-8') as file:
    file.write(jsonData)


# ЧТЕНИЕ ИЗ ФАЙЛА-------------------------------------
print('---------------------------------')

# Откроем файл созданный выше
with open("peoples.json", "r", encoding='UTF-8') as file:
    jsonData=file.read()

# Загрузим json в словарь
dict1 = json.loads(jsonData)

# Пройдемся по словарю
for key in dict1:
    # вытащим из значения вложенный словарь
    dict2 = dict1[key]
    # Напечатаем информацию
    print(key, dict2['name'], dict2['age'], dict2['sex'], dict2['work'])
