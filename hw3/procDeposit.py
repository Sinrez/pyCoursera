percent = int(input())
rouble, penny = int(input()), int(input())
deposit = rouble * 100 + penny
deposit += int(deposit * percent / 100)
rouble = int(deposit / 100)
penny = deposit % 100
print(rouble, penny)
