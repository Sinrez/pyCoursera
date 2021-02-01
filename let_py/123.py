import random

list_ = []
a = {}
for i in range(5):
    a['x'] = random.randint(0, 100)
    list_.append(a)
print(list_)