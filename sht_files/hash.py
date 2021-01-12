# Импортируем в программу библиотеку для шифрования.
import hashlib

# Задаем "сырой" (незашифрованный) пароль.
raw_password = 'password'

# Кодируем "сырой" пароль.
# Нужно для того, чтобы воспользоваться md5.
raw_password = raw_password.encode()

# Получаем шифр-объект.
hash_password = hashlib.md5(raw_password)

# Получаем зашифрованный пароль.
hash_password = hash_password.hexdigest()

# Выводим зашифрованный пароль.
print(hash_password)
#5f4dcc3b5aa765d61d8327deb882cf99

# Именно строка вида "5f4dcc3b5aa765d61d8327deb882cf99"
# обычно хранится в программе или базе данных.