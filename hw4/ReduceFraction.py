a = int(input())  # 1-ая переменная
b = int(input())  # 2-ая переменная


def ReduceFraction(a, b):
    i = 1  # счетчик
    while i < 10:  # мы пытаемся поделить числитель и знаменатель на число от 2 до 10
        i += 1
        if a % i == 0 and b % i == 0:  # если нашли числов на которое поделили без остатка
            return ReduceFraction(a // i, b // i)  # вызываем функцию еще раз и пытаемся снова делить
    return a, b  # если поделить не получилось возвращаем последнии неподеленные числа


a = str(ReduceFraction(a, b))  # так как возвращаются данные в непонятном нам еще формате - преобразуем в строку
print(a[1:a.find(",")], a[a.find(",") + 2:-1])  # убираем из строки все лишнее что бы остались только числа
