# Модуль pickle позволяет сохранять в файлы переменные целиком
# При этом внутри файлов они хранятся в режиме набора байтов
import pickle

# Для примера сохраним в файл список и словарь
a = [1, 10, 0, -3, 9]
b = {'a': 1, 'b': 2}

# Запись переменных в файл
f = open('data', 'wb')
pickle.dump(a, f)
pickle.dump(b, f)
f.close()

# Чтение переменных из файла
f = open('data', 'rb')
c = pickle.load(f)
d = pickle.load(f)
print(c)
print(d)
