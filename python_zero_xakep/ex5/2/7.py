import os

mypath=r'myfiles/test.txt'
mypath2=r'myfiles/'

# Возвращает имя объекта (файл \ папка) указанного пути
s=os.path.basename(mypath)
print(s)
# Возвращает родительский путь к объекту пути
s=os.path.dirname(mypath)
print(s)

# Получаем расширение файла
x, s = os.path.splitext(mypath)
print(s)

# Является ли объект пути обычным файлом? (существующим)
if os.path.isfile(mypath):
    print(mypath + ' - это файл')

# Является ли объект пути обычной папкой? (существующей)
if os.path.isdir(mypath2):
    print(mypath2 + ' - это папка')
