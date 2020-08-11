ten_things = "Яблоки Апельсины Вороны Телефоны Свет Сахар"
#запуск из ком строки
print("Тут меньше 10 объектов, исправим это")
stuff = ten_things.split(' ')

more_stuff = ["День", "Ночь", "песня", "Мишка",
              "Кукуруза", "Банан", "Девочка", "Мальчик"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Добавляем: ", next_one)
    stuff.append(next_one)
    print(f"Теперь у нас {len(stuff)} объектов")

print("Итак: ", stuff)

print("Давайте кое-что сделаем с нашими объектами")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))