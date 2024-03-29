# Словарь —неупорядоченная структура данных,
# которая позволяет хранить пары «ключ — значение»

# Пустой словарь
dict1 ={}

dict2={'Ваня': 'программист',
           'Маша': 'секретарь',
           'Коля': 'менеджер',
           'Саша': 'директор',
           'Павел': 'пентестер'}

# Получаем значение словаря по ключу
print(dict2['Саша'])
# Если ключа нет, будет ошибка
#print(dic2['Даша'])

# Такой вариант при отсутствии ключа вернет None
print(dict2.get('Даша'))

# Заменяем значение определенного элемента словаря
dict2['Маша'] = 'зам.директора'
print(dict2['Маша'])

# Удаляем элемент
del dict2['Коля']
print(dict2)

# Печатаем ключи, значения
print(dict2.keys())
print(dict2.values())

print('_______________\n')

# Проходим циклом по словарю
for key in dict2:
   print(key)
   print(dict2[key])
