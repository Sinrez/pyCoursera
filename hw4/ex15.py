from sys import argv
#запуск из ком строки
script, filename = argv

txt = open(filename)

print(f"Содержимое файда {filename}: ")
print(txt.read())
print("Снова введите имя файла:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()