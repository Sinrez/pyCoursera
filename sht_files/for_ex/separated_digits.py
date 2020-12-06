import sys

args = sys.argv[1:]

# Заводим два списка для отрицательных и положительных чисел.
negative = []
postitve = []

for i in args:
    # Разделяем по спискам.
    if int(i) < 0:
        negative.append(i)
    else:
        postitve.append(i)

# Выводим через пробел.
print(" ".join(negative + postitve))