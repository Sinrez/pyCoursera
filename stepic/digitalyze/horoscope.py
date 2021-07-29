inp_d = input().strip().split(' ')
for d in inp_d:
    if d.isalpha():
        exit('некорректная дата')
month, date = map(int, inp_d)

if (date >= 21 and date <= 31 and month == 3) or (month == 4 and date >= 1 and date <= 19):
    print("Овен")
elif (date >= 20 and date <= 30 and month == 4) or (month == 5 and date >= 1 and date <= 20):
    print("Телец")
elif (date >= 21 and date <= 31 and month == 5) or (month == 6 and date >= 1 and date <= 21):
    print("Близнецы")
elif (date >= 22 and date <= 30 and month == 6) or (month == 7 and date >= 1 and date <= 22):
    print("Рак")
elif (date >= 23 and date <= 31 and month == 7) or (month == 8 and date >= 1 and date <= 22):
    print("Лев")
elif (date >= 23 and date <= 31 and month == 8) or (month == 9 and date >= 1 and date <= 22):
    print("Дева")
elif (date >= 23 and date <= 30 and month == 9) or (month == 10 and date >= 1 and date <= 23):
    print("Весы")
elif (date >= 24 and date <= 31 and month == 10) or (month == 11 and date >= 1 and date <= 22):
    print("Скорпион")
elif (date >= 23 and date <= 30 and month == 11) or (month == 12 and date >= 1 and date <= 21):
    print("Стрелец")
elif (date >= 22 and date <= 31 and month == 12) or (month == 1 and date >= 1 and date <= 20):
    print("Козерог")
elif (date >= 21 and date <= 31 and month == 1) or (month == 2 and date >= 1 and date <= 18):
    print("Водолей")
elif (date >= 19 and date <= 29 and month == 2) or (month == 3 and date >= 1 and date <= 20):
    print("Рыбы")
else:
    print('некорректная дата')
