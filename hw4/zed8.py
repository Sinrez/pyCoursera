from sys import argv
#запускать из ком строки
script, filename = argv

print(f"Я собираюсь стереть файло {filename}.")
print("Если вы не хотите стиреть его, нажмите сочетание клавиш ctrl + c")
print("Если хотите прочитать файл, нажмите клавишу Enter")

input("?")

print("Открытие файла...")
target = open(filename, 'r')
txt = target.read()
print(txt)