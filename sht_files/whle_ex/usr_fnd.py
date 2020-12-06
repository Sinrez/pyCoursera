import sys

idd = int(sys.argv[1])

users = [
    {"id": 17, "first_name": "Дмитрий", "last_name": "Иванов"},
    {"id": 156, "first_name": "Виктор", "last_name": "Осипов"},
    {"id": 23, "first_name": "Алёна", "last_name": "Гордеева"},
    {"id": 84, "first_name": "Семён", "last_name": "Васильев"},
    {"id": 21, "first_name": "София", "last_name": "Зинько"},
    {"id": 55, "first_name": "Антон", "last_name": "Ватутин"},
    {"id": 287, "first_name": "Виталий", "last_name": "Новиков"}
]

i = 0
while(users[i]["id"] != idd):
    i += 1
print(users[i]["first_name"], users[i]["last_name"], sep = ' ')