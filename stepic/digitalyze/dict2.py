import json

# name Пётр phone 02 sex male balance 50000
# inp = ('name Пётр phone 02 sex male balance 50000').split(' ')
# inp = ('1 2 3').split(' ')
# print(inp)
my_dict = {}
dict_keys = []
dict_values = []
inp = input().strip().split(' ')
# print(len(inp))
if len(inp) % 2 != 0:
    inp = inp[:len(inp) - 1]
for i in range(len(inp)):
    if i % 2 == 0:
        dict_keys.append(inp[i])
    else:
        dict_values.append(inp[i])
my_dict = dict(zip(dict_keys, dict_values))
print(json.dumps(my_dict, ensure_ascii=False))


