# Напечатаем список всех файлов содержащихся
# внутри папок по определенному пути (учитывая вложенные подкаталоги)

import os
# Пример с общедоступной папкой для Windows (измените путь для другой ОС)
for root, dirs, files in os.walk(r'C:/Users/Public/'):
    for name in files:
        #print(root)
        #print(name)
        fullname = os.path.join(root, name)
        print(fullname)
