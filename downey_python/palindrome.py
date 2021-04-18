def is_paindrome(sstr):
    if sstr == sstr[::-1]:
        return 'Это палиндром'
    else:
        return 'Это не палиндром'


str_ex = input('Введите слово: ')
print(is_paindrome(str_ex))