# 8.1.. Создайте.англо-французский.словарь.с.названием.e2f.и.выведите.его.на.экран..
# Вот.ваши.первые.слова:.dog/chien,.cat/chat.и.walrus/morse.
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse',
}

# 8.2.. Используя.словарь.e2f,.выведите.французский.вариант.слова.walrus.

print(e2f['walrus'])
print(5*'-')

# 8.3..
# Создайте.французско-английский.словарь.f2e.на.основе.словаря.e2f..
# Используйте.метод.items.

f2e ={}
for en, fr in e2f.items():
    f2e[fr] = en
print(f2e)

# 8.4.. Используя.словарь.f2e,.выведите.английский.вариант.слова.chien.
print(f2e['chien'])
print(5*'-')

# 8.5.. Выведите.на.экран.множество.английских.слов.из.ключей.словаря.e2f.
print(*e2f.keys())

# 8.6.. Создайте.многоуровневый.словарь.life..
# Используйте.следующие.строки.для.
# ключей.верхнего.уровня:.'animals',.'plants'.и.'other'..
# Сделайте.так,.чтобы. ключ.'animals'.ссылался.на.другой.словарь,.
# имеющий.ключи.'cats',.'octopi'. и.'emus'..Сделайте.так,.чтобы.ключ.
# 'cats'.ссылался.на.список.строк.со.значени- ями.'Henri',.'Grumpy'.и.'Lucy'..
# Остальные.ключи.должны.ссылаться.на.пустые. словари.
life = {
    'animals':{
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants':{},
    'other': {}
}

# 8.7.. Выведите.на.экран.высокоуровневые.ключи.словаря.life.
print(life.keys())

# 8.8.. Выведите.на.экран.ключи.life['animals'].
print(life['animals'].keys())

# 8.9.. Выведите.значения.life['animals']['cats'].
print(*life['animals']['cats'])

# 8.10.. Используйте.генератор.словаря,.чтобы.создать.словарь.squares..
# Используйте. range(10),.чтобы.получить.ключи..В.качестве.значений.используйте.возведен-
# ное.в.квадрат.значение.каждого.ключа.
squares = {key: key*key for key in range(10)}
print(squares)

# 8.11.. Используйте.генератор.множества,.чтобы.создать.множество.odd.из.нечетных. чисел.диапазона.range(10).
print(5*'-')
sets = (dg for dg in range(10) if dg % 2 != 0)
print(*sets)

# 8.12.. Используйте.включение.генератора,.чтобы.вернуть.строку.'Got.'.
# и.числа.из. диапазона.range(10)..Итерируйте.по.этой.конструкции.с.помощью.цикла.for.
for s in (f'Got. {i}' for i in range(10)):
    print(s)

# 8.13.. Используйте.функцию.zip(),.чтобы.создать.словарь.из.кортежа.ключей.
# ('optimist',.'pessimist',.'troll').и.кортежа.значений.('The.glass.is.half.full',.
# 'The.glass.is.half.empty',.'How.did.you.get.a.glass?').
cor_keys = ('optimist','pessimist','troll')
cor_val = ('The.glass.is.half.full','The.glass.is.half.empty','How.did.you.get.a.glass?')
d = dict(zip(cor_keys, cor_val))
print(d)

# 8.14.. Используйте.функцию.zip(),.чтобы.создать.словарь.с.
# именем.movies,.в.котором. объединены.списки.titles.=.['Creature.of.Habit',.
# 'Crewel.Fate',.'Sharks.On. a.Plane'].и.plots.=.['A.nun.turns.into.a.monster',
# .'A.haunted.yarn.shop',.'Check. your.exits'].
titles = ['Creature.of.Habit','Crewel.Fate','Sharks.On. a.Plane']
plots = ['A.nun.turns.into.a.monster','A.haunted.yarn.shop','Check. your.exits']

movies = dict(zip(titles, plots))
print(movies)

