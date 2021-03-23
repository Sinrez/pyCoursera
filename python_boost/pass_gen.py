# программу, которая генерирует случайный пароль, соответствующий следующим условиям:
#
# – Длина пароля должна составлять 10 символов
# – Пароль должен содержать как минимум 2 заглавные буквы, 1 цифру и 1 специальный символ

import random
import string
def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    return ''.join(password)
print ("Password is ", randomPassword())