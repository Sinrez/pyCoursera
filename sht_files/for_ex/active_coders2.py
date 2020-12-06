import sys

# Получаем язык.
lang = sys.argv[1]

users = [
    {"id": 17,  "lang": "python", "active": False},
    {"id": 156, "lang": "php",    "active": True},
    {"id": 23,  "lang": "java",   "active": True},
    {"id": 84,  "lang": "python", "active": True},
    {"id": 28,  "lang": "java",   "active": False},
    {"id": 21,  "lang": "java",   "active": True},
    {"id": 55,  "lang": "python", "active": True},
    {"id": 88,  "lang": "python", "active": True},
    {"id": 287, "lang": "c++",    "active": False},
    {"id": 481, "lang": "php",    "active": False},
    {"id": 134, "lang": "c++",    "active": True},
    {"id": 65, "lang": "php",    "active": True},
]

users_ids = []

for user in users:
    # Проверяем языки и активность.
    if user["lang"] == lang and user["active"]:
        # Собираем id
        users_ids.append(user["id"])

# Сортируем результат.
users_ids.sort()

# Приводим к строкам.
i = 0
while i < len(users_ids):
    users_ids[i] = str(users_ids[i])
    i += 1


# Выводим результат
print(", ".join(users_ids))