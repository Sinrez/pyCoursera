
res = []
d = 1
while d!=0:
    d = int(input())
    res.append(d)
s = 0
if d == 0:
    for r in res:
        s += int(r)
print(s)
