import math

weight = input().strip()

if not weight.isdigit():
    # exit('некорректный вес')
    print('некорректный вес')
elif int(weight) > 10000:
    # exit('не возим')
    print('не возим')
elif int(weight) <= 500:
    weight = int(weight)
    # tax = (weight // 100 + weight % 100) * 80
    tax = math.ceil(weight / 100) * 80
    print(tax)
elif 500 < int(weight) <= 1000:
    weight = int(weight)
    tax = math.ceil(weight / 100) * 70
    print(tax)
elif 1000 < int(weight) <= 10000:
    weight = int(weight)
    tax = math.ceil(weight / 100) * 65
    print(tax)
