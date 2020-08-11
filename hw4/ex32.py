the_count = [1, 2, 3, 4, 5]
fruits = ['яблоко', 'апельсин', 'персик', 'абрикос']
change = [1, 'червонэц', 2, 'полтинник', 3, 'сотня']

#запуск из ком строки

for nunber in the_count:
    print(f"Счетчик {nunber}")

for fruit in fruits:
    print(f"Фрукт: {fruit}")

for i in change:
    print(f"Я получил {i}")

elements = []

for i in range(0, 6):
    print(f"Добавление {i} в список")
    elements.append(i)
#выведем их
for i in elements:
    print(f"Номер элемента: {i}")