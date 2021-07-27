names = input('имена: ').split(",")
phones = input('телефоны: ').split(",")

for i in range(len(names)):
    print(f"{names[i]}: {phones[i]}")