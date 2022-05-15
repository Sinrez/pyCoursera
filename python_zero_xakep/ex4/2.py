# Программа которая тестирует наш модуль superfiles
# Импортируем модуль sys чтобы указать папку, где лежат другие модули
import sys
sys.path.append('modules/')
import superfiles as sf

# Загрузим строки из файла в список
mylist = sf.filetolist('files/test.txt')
print(mylist)

print('------------------------')

# Загрузим весь текст файла в переменную
x = sf.filetox('files/test.txt')
print(x)

print('------------------------')

# Добавим в файл строку
sf.addline('files/test.txt', 'Hello world!')
# Добавим в файл список строк
sf.addlist('files/test.txt', ['Элемент 1', 'Элемент 2'])
# Снова прочтем весь текст из файла
x = sf.filetox('files/test.txt')
print(x)

print('------------------------')

# Ищем в каком-то файле строку
if sf.findinfile('files/test.txt', 'Hello world!'):
    print('Нашлась строчка!')

print('------------------------')

# Записываем список строк в файл
mylist2 = ['1','2','3']
sf.listtofile('files/123.txt', mylist2)

print('------------------------')

# Загружаем из файла строки, в которых части строк разделены каким-то разделителем
x = sf.filetosplitlist('files/testsep.txt', '|')
for s in x:
    print(s)
