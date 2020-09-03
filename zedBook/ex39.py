#схема связей аббревиатур со странами, запуск из ком строки
states = {
    'Russia': 'RU',
    'Germany': 'DE',
    'Uzbekistan': 'UZ',
    'France': 'FR',
    'Turkey': 'TR'
}

#создание базового набора стран и городов
cities = {
    'UZ': 'Газли',
    'TR': 'Сарыгерме',
    'DE': 'Мюнхнен'
}

#добавление нескольких городов
cities['FR'] = 'Париж'
cities['RU'] = 'Москва'

#Вывод нескольких городофффф
print('-' * 10)
print("В стране FR есть город: ", cities['FR'])
print("В стране RU есть город: ", cities['RU'])

#вывод нескольких стран
print('-' * 10)
print("Аббревиатура Турции: ", states['Turkey'])
print("Аббревиатура Германии: ", states['Germany'])

#выполняется с учетом страны и словаря городов
print('-' * 10)
print("В Турции есть город: ", cities[states['Turkey']])
print("В Германии есть город: ", cities[states['Germany']])

#вывод аббревиатур  всех стран
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} имеет аббревиатуру {abbrev}")

#вывод всех городов в странах
print('-' * 10)
for abbrev, city in list(states.items()):
    print(f"в стране  {state} есть город {city}")

#а теперь сразу оба типа данных нах:
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} используется аббревиатура {abbrev}")
    print(f"в стране  {state} есть город {cities[abbrev]}")

print('-' * 10)
# дофига безопасное получение аббревиатуры страны, которая не представлена
state = states.get('США')

if not state:
    print("США нет")

# получение города со значением по умолчанию
city = cities.get('US', 'не существует')
print(f"В стране 'US' есть город {city}")