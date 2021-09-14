import csv
import struct


with open("sport_food.csv", encoding='windows-1251') as sport:
    with open("sport_food.bin", "wb") as sport_food:
        sp = csv.DictReader(sport)
        x = 0
        new = struct.pack("I", x)
        sport_food.write(new)
        for i in sp:
            prod = struct.pack("100sHH", i['Название'].encode(encoding="UTF-8"), int(i['Вес']), int(i['Стоимость']))
            sport_food.write(prod)
            x += 1
        sport_food.seek(0)
        new_2 = struct.pack("I", x)
        sport_food.write(new_2)