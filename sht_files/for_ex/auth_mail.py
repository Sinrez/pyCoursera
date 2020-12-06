import sys

mail = sys.argv[1].lower()
pasw = sys.argv[2]

users = [
    {"email": "user1@domain.com", "password": "password1"},
    {"email": "user2@domain.com", "password": "abcde"},
    {"email": "user3@domain.com", "password": "123456"},
    {"email": "user4@domain.com", "password": "lovelove"},
    {"email": "user5@domain.com", "password": "kdmUdmk84M"}
]

# print(mail)
# print(pasw)
fnd = False
for user in users:
    if (mail in user["email"]):
        fnd = True
    else:
        pass

if (fnd == False):
    print("Пользователь не найден")

for user in users:
    if (fnd == True):
        if (user["email"] == mail and user["password"] == pasw):
            print("Доступ открыт")
            break
        elif (user["email"] == mail and user["password"] != pasw):
            print("Доступ закрыт")
            break