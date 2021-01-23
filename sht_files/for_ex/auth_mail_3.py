import sys

users = [
    {"email": "user1@domain.com", "password": "password1"},
    {"email": "user2@domain.com", "password": "abcde"},
    {"email": "user3@domain.com", "password": "123456"},
    {"email": "user4@domain.com", "password": "lovelove"},
    {"email": "user5@domain.com", "password": "kdmUdmk84M"}
]

# Получаем данные пользователя.
email = sys.argv[1].lower()
password = sys.argv[2]

# Задаем доступ: None - пользователь не найден, True - доступ есть, False - доступа нет.
has_access = None

# Перебираем всех пользователей в цикле:
for user in users:
    if user["email"] == email:
        if user["password"] == password:
            has_access = True
        else:
            has_access = False

        break

# Выводим результат.
if has_access is None:
    print("Пользователь не найден")
elif has_access:
    print("Доступ открыт")
else:
    print("Доступ закрыт")