# Счастливым называют такой билет, что сумма первых трех цифр
# его номера равна сумме последний трех цифр.
# Встречным называют такой билет,
# что сумма первых трех цифр его номера отличается на единицу от суммы последних трех цифр.
# Пьяным называют такой билет,
# что сумма первых трех цифр его номера отличается на двойку от суммы последних трех цифр.
# Обычными называют все остальные билеты.
def ticket_type(sstr):
    HAPPY = 'счастливый'
    ONCIMING = 'встречный'
    DRUNK = 'пьяный'
    SIMPLE = 'обычный'
    lst =[]
    for s in sstr:
        lst.append(s)
    first_three = int(lst[0])+int(lst[1])+int(lst[2])
    second_three = int(lst[3])+int(lst[4])+int(lst[5])
    if first_three == second_three:
        result = HAPPY
    elif first_three - second_three == 1 or second_three-first_three ==1:
        result = ONCIMING
    elif first_three - second_three == 2 or second_three-first_three == 2:
        result = DRUNK
    else:
        result = SIMPLE
    return result

#
# result = ticket_type("123602")
# print(result)
