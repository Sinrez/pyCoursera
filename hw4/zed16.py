print("you практикуем")
print('управленеи посл с символом \\, которые:')
print('\n  управляют переносом строк и \t отступами')
#запуск из ком строки
poem = """
\tдля тттт
бла бла бла
"""
print("--------------------")
print(poem)
print("--------------------")

five = 10 - 2 + 3 - 6
print(f"Здесь должна быть пятерка: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000

beans, jars, creates = secret_formula(start_point)

#помните, что это еще один  способ форматирования строки

print("Начиная с {}".format(start_point))
#так же, как со строкой f""
print(f"У нас есть {beans} бобов, {jars} банок и {creates} ящиков")

start_point = start_point / 10

print("Мы также млжем сделать это таким образом:")
formula = secret_formula(start_point)

print("У нас есть {} бобов, {} банок и {} ящиков.".format(*formula))