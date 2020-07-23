#import divide as divide


def add(a, b):
    print(f"Сложение  {a} + {b}")
    return a + b
#запускать из комм строки
def subtract(a, b):
    print(f"Вычитание  {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Умножение  {a} * {b}")
    return a - b

def divide(a, b):
    print(f"Деление  {a} / {b}")
    return a / b

print("Давайте выполним несколько вычислений с помощью функций")

age = add(30, 5)
height = subtract(190, 4)
weight = multiply(35, 2)
iq = divide(250, 2)

print("Головоломка")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))