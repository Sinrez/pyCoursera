import sys
text = sys.argv[1]

words = []
# Разбиваем текст на слова и проходим по ним в цикле
for word in text.split(" "):
    # Каждое отдельное слово разворачиваем с помощью среза [::-1]
    # и добавляем в список words
    words.append(word[::-1])

# Склеиваем все слова обратно с помощью join
print(" ".join(words))