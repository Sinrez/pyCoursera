import sys

products = ["Молоко", "Масло", "Хлеб", "Овсянка", "Яйца"]

# Получаем товар.
product = sys.argv[1]

# Проверяем, находится ли товар product в списке products.
if product not in products:
    products.append(product)

# Сортируем список.
products.sort()

print(", ".join(products))