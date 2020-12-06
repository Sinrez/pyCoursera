import sys

password = sys.argv[1]

# Используем функцию len()
if len(password) < 6:
    print("Пароль слишком короткий")
# Используем метод __len__()
elif 6 <= password.__len__() <= 8:
    print("Хорошо, но можно и лучше")
else:
    print("Пароль подходит")

# Функция len() и метод __len__() равнозначны