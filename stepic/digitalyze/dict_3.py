import json

inp = input().strip()
if not inp.isdigit():
    print('передайте число')
    exit()
dict = {}
inp = int(inp)
for i in range(1, inp + 1):
    dict[i] = i ** 2

print(json.dumps(dict, ensure_ascii=False))
