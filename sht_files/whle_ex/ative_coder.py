import sys

# Получаем язык.
lang = sys.argv[1]


users = [
    {"id": 17,  "lang": "python", "active": False},
    {"id": 156, "lang": "php",    "active": True},
    {"id": 23,  "lang": "java",   "active": True},
    {"id": 84,  "lang": "python", "active": True},
    {"id": 21,  "lang": "java",   "active": False},
    {"id": 55,  "lang": "python", "active": True},
    {"id": 88,  "lang": "python", "active": True},
    {"id": 287, "lang": "c++",    "active": False},
    {"id": 481, "lang": "php",    "active": False},
    {"id": 134, "lang": "c++",    "active": True}
]


i = 0

# Перебираем всех программистов
while i < len(users):
    # Получаем данные очередного программиста.
    user = users[i]

    # Проверяем языки и активность.
    if user["lang"] == lang and user["active"]:
        # Выводим данные и завершаем цикл.
        print(user["id"])
        break

    i += 1