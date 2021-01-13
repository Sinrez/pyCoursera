import sys

strr = sys.argv[1:]
res = []
for i in strr:
    if i == 'null':
        continue
    else:
        res.append(i)
print(res)