import os
 
# Читаем строки из файла, возвращаем список строк
def filetolist(filename, encoding='UTF-8'):
    if not os.path.exists(filename):
        print('FILE NOT FOUND!')
        return None
    f = open(filename, 'r', encoding=encoding)
    mylist =[]
    for x in f:
        mylist.append(x)
    f.close()
    return mylist

# Читаем сразу всё содержимое файла
def filetox(filename, encoding='UTF-8'):
    if not os.path.exists(filename):
        print('FILE NOT FOUND!')
        return None
    f = open(filename, 'r', encoding=encoding)
    s = f.read()
    f.close()
    return s

# Добавляем строку в файл
def addline(filename, line, encoding='UTF-8'):
    if not os.path.exists(filename):
        print('FILE NOT FOUND!')
        return None
    f = open(filename, 'a', encoding=encoding)
    f.write(line+'\n')
    f.close()
    return 1

# Добавляем в файл список строк
def addlist(filename, lines, encoding='UTF-8'):
    if not os.path.exists(filename) and lines!=[]:
        print('FILE NOT FOUND!')
        return None
    f = open(filename, 'a', encoding=encoding)
    for x in lines:
        f.write(x+'\n')
    f.close()
    return len(lines)

# Поиск строки в файле
def findinfile(filename, text, encoding='UTF-8'):
    if not os.path.exists(filename):
        print('FILE NOT FOUND!')
        return None
    f = open(filename, 'r', encoding=encoding)
    for x in f:
        if x.strip() == text.strip():
            return True
    f.close()
    return False

# Сохраняем список в файл
def listtofile(filename, mylist, encoding='UTF-8'):
    f = open(filename, 'w', encoding=encoding)
    for x in mylist:
        f.write(x.strip()+'\n')
    f.close()

# Читаем из файла строки, и части строк разделенных разделителем
# Получаем вложенный список
def filetosplitlist(filename, sep, encoding='UTF-8'):
    if not os.path.exists(filename):
        print('FILE NOT FOUND!')
        return None
    f = open(filename, 'r', encoding=encoding)
    mylist =[]
    for x in f:
        if x.strip()!='':
            list1 = x.split(sep)
            mylist.append(list1)
    f.close()
    return mylist
       
if __name__ == "__main__":
    print('Это не скрипт а модуль!')
 
