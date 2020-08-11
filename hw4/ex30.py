people = 30
cars = 40
trucks = 15
#запуск из ком строки
if cars > people:
    print("Поедем на машине")
elif cars < people:
    print("Не поедем на машине")
else:
    print("Мы не можем выбрать")

if trucks > cars:
    print("Слишком много автобусов")
elif trucks < cars:
    print('МОжет поехать на автобусе?')
else:
    print("Мы до сих пор не можем выбрать")

if people > trucks:
    print("Хорошо, едем на автобусе")
else:
    print("Прекрасно, остаемся дома")