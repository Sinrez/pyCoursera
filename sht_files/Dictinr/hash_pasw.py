import sys
import hashlib

# Зашифрованный пароль.
hash_password = "c8b667f4e6953d59b6ae9b9659772333"

# Получаем пароль.
user_password = sys.argv[1]

# Кодируем пароль.
user_password = user_password.encode()

# Получаем шифр-объект.
hash_user_password = hashlib.md5(user_password)

# Получаем зашифрованный пароль.
hash_user_password = hash_user_password.hexdigest()

# Проверяем пароль.
if hash_password == hash_user_password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")