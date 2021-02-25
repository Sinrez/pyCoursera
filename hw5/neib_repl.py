l = list(map(int, input().split()))
res = []
for i in range(len(l) - 1):
    if i % 2 == 0:
        res.append(l[i + 1])
        res.append(l[i])
if len(l) % 2 != 0:
    res.append(l[-1])

print(' '.join(map(str, res)))
