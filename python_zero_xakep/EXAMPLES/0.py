# Чтобы работать с каким-либо файлом, его нужно открыть. 
# f = open('Путь к файлу c расширением', 'Режим работы', encoding='Кодировка')

#Режимов работы с файлами несколько, но нас интересует в основном:
# 'r' - открыть файл для чтения с него информации
# 'w' - открыть файл для записи в него информации (создаёт новый файл)
# 'a' - открытие файла для дозаписи информации в конец файла
# (дописывает информацию в конец существующего файла)

# Открываем файл names.txt для чтения 
f = open('myfiles/names1.txt', 'r', encoding='UTF-8')
# С помощью цикла последовательно читаем из файла строки в переменную s
for s in f:
    # Обрезаем с помощью .strip() перенос строки в конце строки
    # печатаем её
    print(s.strip())
# Закрываем файл
f.close()

print('\n-------------\n')

# Файл можно открыть с помощью with
# тогда f.close() писать необязательно - файл закроется как только закончатся
# команды отделенные 4 пробелами
with open('myfiles/text.txt', 'r', encoding='UTF-8') as f:
    # Можно прочитать сразу весь текст из файла в какую-то переменную
    x = f.read()
    print(x)

# Запись в файл
# Возьмем какой-нибудь список строк
mylist = ['Джон', 'Алиса', 'Боб']
# Откроем файл для записи в него строк
f = open('result/names2.txt', 'w', encoding='UTF-8')
# В цикле пройдемся по списку mylist
for x in mylist:
    # Запишем текущее значение x в файл, добавив перенос строки
    f.write(x+'\n')
# Закроем файл
f.close()