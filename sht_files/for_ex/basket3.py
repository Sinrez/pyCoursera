import sys
price = int(sys.argv[1])
products = [
    {"name": "Гречка", "price": 69},
    {"name": "Хлеб", "price": 34},
    {"name": "Молоко", "price": 57},
    {"name": "Яйца", "price": 78},
    {"name": "Рис", "price": 88},
    {"name": "Макароны", "price": 49},
    {"name": "Сахар", "price": 22},
    {"name": "Яблоки", "price": 79},
    {"name": "Картофель", "price": 18},
    {"name": "Свинина", "price": 120},
    {"name": "Масло", "price": 66},
    {"name": "Помидоры", "price": 64}
]
bask = []
for product in products:
    if product["price"] <= price:
        bask.append(product["name"])
        price -= product["price"]
    else:
        continue
y = ", ".join(bask)
print (y)
