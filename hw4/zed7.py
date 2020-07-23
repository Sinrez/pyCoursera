from sys import argv
#запускать из ком строки
script, filename = argv

print(f"Я собираюсь стереть файло {filename}.")
print("Если вы не хотите стиреть его, нажмите сочетание клавиш ctrl + c")
print("Если хотите стереть файл, нажмите клавишу Enter")

input("?")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла. До свидания!")
target.truncate()

print("Теперь я запрашиваю у вас три строки.")

line1 = input("строка 1: ")
line2 = input("строка 2: ")
line3 = input("строка 3: ")

print("Это я запишу в файл")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n" )
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("И наконец, я закрою файл")
target.close()