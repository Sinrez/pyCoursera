# import sys
# for place in sys.path:
#      print(place)

# 11.5.. Создайте.словарь.с.именем.plain,.содержащий.пары.«ключ.—.значение».'a':.1,.
# 'b':.2.и.'c':3,.а.затем.выведите.его.на.экран.
from pprint import pprint
plain = {'a' : 1,'b' : 2, 'c' :3}
pprint(plain)
print(*plain)

# 11.6.. Создайте.OrderedDict.с.именем.fancy.из.пар.«ключ.—.значение»,.приведенных.
# в.упражнении.11.5,.и.выведите.его.на.экран..Изменился.ли.порядок.ключей?

from collections import OrderedDict
fancy = OrderedDict(plain)
print('*' * 20)
for f in fancy:
     print(f)

# 11.7.. Создайте.defaultdict.с.именем.dict_of_lists.и.передайте.ему.аргумент.
# list..Создайте.список.dict_of_lists['a'].и.присоедините.к.нему.значение.
# 'something.for.a'.за.одну.операцию..Выведите.на.экран.dict_of_lists['a'].

from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])
