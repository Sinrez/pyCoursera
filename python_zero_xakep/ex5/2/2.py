# Подключим модуль os
# отвечающий за взаимодействие с файловой системой os
import os
import fnmatch
import shutil

# Получим путь до текущей директории (папки из которой запущен скрипт)
s=os.getcwd()
print(s)

# os.chdir(r'D:/') - можно установить текущей папкой любую другую,
# но тогда все дополнительные файлы система будет искать в ней, а не в папке со скриптом

# Попробуем получить список файлов в текущей директории с расширением '.py'
# Проходим в цикле по всем файлам текущей папки
for file in os.listdir('.'):
    # Проверяем похоже ли имя файла на указанную строку-маску
    if fnmatch.fnmatch(file, '*.py'):
        print(file)

if(os.path.exists(r'myfiles/test.txt')):
    print('Файл test.txt существует')
else:
    print('Файла test.txt не существует')

# Создадим в текущем каталоге папку
if(not os.path.exists(r'test_dir')):
    os.mkdir('test_dir')

# Проверим есть ли файл del.txt в папке myfiles
# Удалим файл если оне есть
if(os.path.exists(r'myfiles/del.txt')):
    os.remove(r'myfiles/del.txt')
    print('Удалили del.txt')

#Переименуем файл:
if(os.path.exists(r'myfiles/file1.txt')):    
    os.rename(r'myfiles/file1.txt', r'myfiles/file2.txt')
    print('Переименовали файл file1.txt в file2.txt')

# Скопируем файл myfiles/test.txt в myfiles/copyfiles/test.txt
shutil.copy2(r'myfiles/test.txt', r'myfiles/copyfiles/test.txt')
print('Скопировали файл myfiles/test.txt в myfiles/copyfiles/test.txt')
