# Модуль для работы с json - текстовым форматом обмена данными
import json

# ЗАПИСЬ В JSON ФАЙЛ

# Создадим словарь с какими-то ключами и значениями
dictData = { "ID"       : 310450,
             "login"    : "admin",
             "name"     : "James Bond",
             "password" : "root",
             "phone"    : 3330303,
             "email"    : "bond@mail.com",
             "online"   : True }

# Преобразуем словарь в json строчку
jsonData = json.dumps(dictData)
print(jsonData)

# Запишем в файл
with open("data.json", "w", encoding='UTF-8') as file:
    file.write(jsonData)

# ЧТЕНИЕ JSON ФАЙЛА-----------------------------------------

# Прочтем ранее созданный файл
with open("data.json", "r", encoding='UTF-8') as file:
    jsonData=file.read()

# Преобразуем json строку в словарь
dictData = json.loads(jsonData)

# Напечатаем некоторые значения из полученного словаря
print(dictData["name"])
print(dictData["phone"])
print(dictData["email"])
print(dictData["online"])

