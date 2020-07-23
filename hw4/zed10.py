from sys import argv
from os.path import exists
#запускать из ком строки
script, from_file, to_file = argv

print(f"Копирование данных из файла {from_file} в файл {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"Исходный файл имеет размер {len(indata)} байт")

print(f"Целевой файл имеет размер {len(indata)} байт")

print(f"Целевой файл существует? {exists(to_file)}")
print("Готов, нажмите клавишу Enter для продолжения или ctrl + c для отмены")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Отлично все готово")

out_file.close()
in_file.close()